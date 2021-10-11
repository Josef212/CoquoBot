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
        user = self.get_username_from_update(update)
        lang = self.get_user_lang_from_update(update)
        chat_id = self.get_chat_id(update)

        msg = self.get_cmd_msg(chat_id, lang, user)
        markup = self.build_edit_order_keyboard(chat_id, user, lang)

        self.update_reply_message(update, msg, markup)

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
                self.inline_btn('-', remove_cbk_data),
                self.inline_btn(msg, ignore_cbk_data),
                self.inline_btn('+', add_cbk_data),
            ])
        
        if len(keyboard) == 0:
            return None
        
        finish = loc.get_text(lang, LocKeys.BTN_FINISH)
        keyboard.append([self.inline_btn(finish, f'{self.__finish}{user}')])

        return self.build_keyboard(keyboard)

    def __ignore_cbk(self, update: Update, ctx):
        update.callback_query.answer()
    
    def __item_cbk(self, update: Update, ctx) -> None:
        query = update.callback_query
        query.answer()

        args = self.get_inline_btn_args_from_query(query)
        user = args[1] # TODO: If we actually can get user that clicked we should get it and remove the user encoded on the cbk_data
        mode = args[2]
        item = args[3]
        modifier = 1 if mode == ADD_KEY else -1
        chat_id = self.get_chat_id(query)
        lang = self.get_user_lang_from_query(query)

        self.app.add_to_order(chat_id, user, item, modifier)

        msg = self.get_cmd_msg(chat_id, lang, user)
        markup = self.build_edit_order_keyboard(chat_id, user, lang)

        self.query_edit_message(query, msg, markup)

    def __finish_cbk(self, update: Update, ctx) -> None:
        query = update.callback_query
        query.answer()

        args = self.get_inline_btn_args_from_query(query)
        user = args[1] # TODO: If we actually can get user that clicked we should get it and remove the user encoded on the cbk_data
        chat_id = self.get_chat_id(query)
        lang = self.get_user_lang_from_query(query)

        get_order_cmd = self.app.get_command('get_order_for')
        full_order = self.app.get_user_order(chat_id, user)
        title = self.app.localization.get_text_format(lang, LocKeys.EDIT_ORDER_TITLE_UPDATED, user)
        msg = get_order_cmd.format_order_with_title(full_order, title, lang)

        self.query_edit_message(query, msg, None)
