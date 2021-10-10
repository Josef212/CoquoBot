from command import Command
from loc_keys import LocKeys

from telegram import Update
from telegram.ext import CallbackQueryHandler

class CmdCoquo(Command):
    def __init__(self, app):
        super().__init__(app)
        self.name = ["coquo"]
        self.__cbk_key = 'coquo#'

        app.dispatcher.add_handler(CallbackQueryHandler(lambda u, c: self.__item_cbk(u, c), pattern=f'^{self.__cbk_key}'))
    
    def execute(self, update: Update, ctx) -> None:
        user = self.get_username_from_update(update)
        lang = self.get_user_lang_from_update(update)

        msg = self.app.localization.get_text(lang, LocKeys.COQUO_OPTIONS)
        markup = self.__create_markup(user, lang)

        self.update_reply_message(update, msg, markup)

    def __item_cbk(self, update: Update, ctx) -> None:
        query = update.callback_query
        query.answer()

        lang = self.get_user_lang_from_query(query)
        args = self.get_inline_btn_args_from_query(query)
        chat_id = self.get_chat_id(query)
        user = args[1]
        action = args[2]

        loc = self.app.localization

        if action == LocKeys.BTN_MENU:
            # TODO: Use something like get_command_by_type
            msg = self.app.get_command('menu').get_menu_text()
            self.query_reply_message(query, msg)
        elif action == LocKeys.BTN_WEB:
            msg = self.app.menu.get_menu_web()
            self.query_reply_message(query, msg)
        elif action == LocKeys.BTN_RESET_ORDER:
            self.app.reset_order(chat_id)
            msg = loc.get_text(lang, LocKeys.ORDER_RESET_DONE)
            self.query_edit_message(query, msg, None)
        elif action == LocKeys.BTN_ORDER:
            pass
        elif action == LocKeys.BTN_EDIT_ORDER:
            pass
        elif action == LocKeys.BTN_GET_MY_ORDER:
            pass
        elif action == LocKeys.BTN_GET_FULL_ORDER:
            pass
        elif action == LocKeys.BTN_FINISH:
            msg = loc.get_text(lang, LocKeys.COQUO_FINISHED)
            self.query_edit_message(query, msg, None)
        
    def __create_markup(self, user: str, lang: str):
        key = self.__cbk_key
        loc = self.app.localization

        keyboard = [
            [
                self.inline_btn(loc.get_text(lang, LocKeys.BTN_MENU), f'{key}{user}#{LocKeys.BTN_MENU}'),
                self.inline_btn(loc.get_text(lang, LocKeys.BTN_WEB), f'{key}{user}#{LocKeys.BTN_WEB}'),
                #self.inline_btn(loc.get_text(LocKeys.BTN_RESET_ORDER), f'{key}{user}#{LocKeys.BTN_RESET_ORDER}')
            ],
            [
                self.inline_btn(loc.get_text(lang, LocKeys.BTN_ORDER), f'{key}{user}#{LocKeys.BTN_ORDER}'),
                self.inline_btn(loc.get_text(lang, LocKeys.BTN_EDIT_ORDER), f'{key}{user}#{LocKeys.BTN_EDIT_ORDER}')
            ],
            [
                self.inline_btn(loc.get_text(lang, LocKeys.BTN_GET_MY_ORDER), f'{key}{user}#{LocKeys.BTN_GET_MY_ORDER}'),
                self.inline_btn(loc.get_text(lang, LocKeys.BTN_GET_FULL_ORDER), f'{key}{user}#{LocKeys.BTN_GET_FULL_ORDER}')
            ],
            [
                self.inline_btn(loc.get_text(lang, LocKeys.BTN_FINISH), f'{key}{user}#{LocKeys.BTN_FINISH}')
            ]
        ]

        return self.build_keyboard(keyboard)