from command import Command
from loc_keys import LocKeys

from telegram import Update
from telegram.ext import CallbackQueryHandler

class CmdOrder(Command):
    def __init__(self, app):
        super().__init__(app)
        self.name = ["order"]
        self.__key = 'order#'
        self.__finish_key = 'order_finish#'

        app.dispatcher.add_handler(CallbackQueryHandler(lambda u, c: self.__item_cbk(u, c), pattern=f'^{self.__key}'))
        app.dispatcher.add_handler(CallbackQueryHandler(lambda u, c: self.__finish_cbk(u, c), pattern=f'^{self.__finish_key}'))
    
    def execute(self, update: Update, ctx) -> None:
        user = self.get_username_from_update(update)
        lang = self.get_user_lang_from_update(update)

        msg = self.get_cmd_msg(lang)
        markup = self.build_order_keyboard(user, lang)

        self.update_reply_message(update, msg, markup)

    def get_cmd_msg(self, lang: str) -> str:
        return self.app.localization.get_text(lang, LocKeys.ORDER_MSG)

    def build_order_keyboard(self, user: str, lang: str):
        # TODO: Must add pagination to this keyboard
        # TODO: As a simple solution could add two columns 

        keyboard = list()
        menu = self.app.menu
        for item in menu.get_menu_list():
            # TODO: Localize each item??
            cbk_data = f'{self.__key}{user}#{item}'
            keyboard.append([self.inline_btn(item, cbk_data)])

        finish = self.app.localization.get_text(lang, LocKeys.BTN_FINISH)
        keyboard.append([self.inline_btn(finish, f'{self.__finish_key}{user}')])

        return self.build_keyboard(keyboard)

    def __item_cbk(self, update: Update, ctx) -> None:
        query = update.callback_query
        query.answer()

        args = self.get_inline_btn_args_from_query(query)
        user = args[1] # TODO: If we actually can get user that clicked we should get it and remove the user encoded on the cbk_data
        item = args[2]
        chat_id = self.get_chat_id(query)
        lang = self.get_user_lang_from_query(query)

        current_text = query.message.text
        text = self.app.localization.get_text_format(lang, LocKeys.ORDER_ITEM_ADDED, item, user)
        current_text += f'  - {text}'

        self.app.add_to_order(chat_id, user, item, 1)
        # TODO: Markup replied should take into account pagination
        self.query_edit_message(query, current_text, query.message.reply_markup)

    def __finish_cbk(self, update: Update, ctx) -> None:
        query = update.callback_query
        query.answer()

        args = self.get_inline_btn_args_from_query(query)
        user = args[1] # TODO: If we actually can get user that clicked we should get it and remove the user encoded on the cbk_data
        chat_id = self.get_chat_id(query)
        lang = self.get_user_lang_from_query(query)

        msg = self.app.get_command('get_order_for').get_user_order_text(chat_id, user, lang)
        text = self.app.localization.get_text(lang, LocKeys.ORDER_FINISH_TITLE)
        msg = f'{text}\n  {msg}'

        self.query_edit_message(query, msg, None)