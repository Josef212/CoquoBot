from threading import Lock
from command import Command
from loc_keys import LocKeys

from telegram import Update
from telegram.ext import CallbackQueryHandler

ADD_KEY='ADD_KEY'
REMOVE_KEY='REMOVE_KEY'

class CmdEditOrder(Command):
    def __init__(self, app):
        super().__init__(app)
        self.name = ["edit_order"]

        self.__key = 'edit_order#'
        self.__finish = 'edit_finish#'
        self.__ignore = 'edit_ignore#'

        app.dispatcher.add_handler(CallbackQueryHandler(lambda u, c: self.__item_cbk(u, c), pattern=f'^{self.__key}'))
        app.dispatcher.add_handler(CallbackQueryHandler(lambda u, c: self.__finish_cbk(u, c), pattern=f'^{self.__finish}'))
        app.dispatcher.add_handler(CallbackQueryHandler(lambda u, c: self.__ignore_cbk(u, c), pattern=f'^{self.__ignore}'))
    
    def execute(self, update: Update, ctx) -> None:
        user = self.__try_get_user_from_args(update)
        user = user if user != None else self._get_username()
        lang = self._get_user_lang()
        chat_id = self._get_chat_id()

        msg = self.get_cmd_msg(chat_id, lang, user)
        markup = self.build_edit_order_keyboard(chat_id, user, lang)

        self._reply_message(msg, markup)

    def get_cmd_msg(self, chat_id: int, lang: str, user: str) -> str:
        has_order = self.app.user_has_any_order(chat_id, user)
        loc = self.app.localization

        msg = loc.get_text_format(lang, LocKeys.EDIT_ORDER_USER_ORDER, user)
        if not has_order:
            text = loc.get_text(lang, LocKeys.EDIT_ORDER_EMPTY)
            msg += f'\n  {text}'

        return msg

    def build_edit_order_keyboard(self, chat_id: int, user: str, lang: str):
        loc = self.app.localization
        order = self.app.get_user_order(chat_id, user)
        cart = order['cart']
        keyboard = list()

        for item in cart:
            amount = cart[item]
            msg = f'{amount}x {item}'
            add_cbk_data = f'{self.__key}{user}#{ADD_KEY}#{item}'
            ignore_cbk_data = f'{self.__key}{user}' # TODO: Maybe instead of an add button simply using item btn as add
            remove_cbk_data = f'{self.__key}{user}#{REMOVE_KEY}#{item}'

            keyboard.append([
                self._inline_btn('-', remove_cbk_data),
                self._inline_btn(msg, ignore_cbk_data),
                self._inline_btn('+', add_cbk_data),
            ])
        
        if len(keyboard) == 0:
            return None
        
        finish = loc.get_text(lang, LocKeys.BTN_FINISH)
        keyboard.append([self._inline_btn(finish, f'{self.__finish}{user}')])

        return self._build_keyboard(keyboard)

    def __ignore_cbk(self, update: Update, ctx):
        self._set_cmd_data(update, ctx)
        update.callback_query.answer()
    
    def __item_cbk(self, update: Update, ctx) -> None:
        self._set_cmd_data(update, ctx)
        query = update.callback_query
        query.answer()

        args = self._get_inline_btn_args_from_query(query)
        user = args[1] # TODO: If we actually can get user that clicked we should get it and remove the user encoded on the cbk_data
        mode = args[2]
        item = args[3]
        modifier = 1 if mode == ADD_KEY else -1
        chat_id = self._get_chat_id()
        lang = self._get_user_lang()

        self.app.add_to_order(chat_id, user, item, modifier)

        msg = self.get_cmd_msg(chat_id, lang, user)
        markup = self.build_edit_order_keyboard(chat_id, user, lang)

        self._query_edit_message(query, msg, markup)

    def __finish_cbk(self, update: Update, ctx) -> None:
        self._set_cmd_data(update, ctx)
        query = update.callback_query
        query.answer()

        args = self._get_inline_btn_args_from_query(query)
        user = args[1] # TODO: If we actually can get user that clicked we should get it and remove the user encoded on the cbk_data
        chat_id = self._get_chat_id()
        lang = self._get_user_lang()

        get_order_cmd = self.app.get_command('get_order_for')
        full_order = self.app.get_user_order(chat_id, user)
        title = self.app.localization.get_text_format(lang, LocKeys.EDIT_ORDER_TITLE_UPDATED, user)
        msg = get_order_cmd.format_order(full_order, title, lang)

        self._query_edit_message(query, msg, None)

    def __try_get_user_from_args(self, update: Update) -> str:
        query = update.callback_query
        if query != None:
            return None

        args = update.message.text.split()
        if len(args) >= 2:
            # Will assume name is the first argument and ignore if more arguments are sent
            user = args[1]
            if len(user) == 0:
                return None

            if user[0] == '@':
                user = user[1:]

            # TODO: Check if the user is on the chat
            self.app.info(f'Found user {user} as argument to the command.')
            return user
        
        return None
