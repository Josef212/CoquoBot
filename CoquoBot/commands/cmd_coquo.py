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
        user = self._get_username()
        lang = self._get_user_lang()

        msg = self.app.localization.get_text(lang, LocKeys.COQUO_OPTIONS)
        markup = self.__create_markup(user, lang)

        self._reply_message(msg, markup)

    def __item_cbk(self, update: Update, ctx) -> None:
        self._set_cmd_data(update, ctx)
        query = update.callback_query
        query.answer()

        lang = self._get_user_lang()
        args = self._get_inline_btn_args_from_query(query)
        chat_id = self._get_chat_id()
        action = args[2]

        loc = self.app.localization
        # TODO: Use something like get_command_by_type

        if action == LocKeys.BTN_MENU:
            self._execute_command('menu')
        elif action == LocKeys.BTN_WEB:
            self._execute_command('web')
        elif action == LocKeys.BTN_RESET_ORDER:
            self.app.reset_order(chat_id)
            msg = loc.get_text(lang, LocKeys.ORDER_RESET_DONE)
            self._send_message(msg, None)
        elif action == LocKeys.BTN_ORDER:
            self._execute_command('order')
        elif action == LocKeys.BTN_EDIT_ORDER:
            self._execute_command('edit_order')
        elif action == LocKeys.BTN_GET_MY_ORDER:
            self._execute_command('get_my_order')
        elif action == LocKeys.BTN_GET_FULL_ORDER:
            self._execute_command('get_full_order')
        elif action == LocKeys.BTN_DIVIDED_ORDER:
            self._execute_command('get_full_order_div')
        elif action == LocKeys.BTN_FINISH:
            msg = loc.get_text(lang, LocKeys.COQUO_FINISHED)
            self._query_edit_message(query, msg, None)
        
    def __create_markup(self, user: str, lang: str):
        key = self.__cbk_key
        loc = self.app.localization

        keyboard = [
            [
                self._inline_btn(f'🍕 {loc.get_text(lang, LocKeys.BTN_ORDER)}', f'{key}{user}#{LocKeys.BTN_ORDER}'),
                self._inline_btn(f'📑 {loc.get_text(lang, LocKeys.BTN_EDIT_ORDER)}', f'{key}{user}#{LocKeys.BTN_EDIT_ORDER}')
            ],
            [
                self._inline_btn(f'🛒 {loc.get_text(lang, LocKeys.BTN_GET_MY_ORDER)}', f'{key}{user}#{LocKeys.BTN_GET_MY_ORDER}'),
                self._inline_btn(f'📜 {loc.get_text(lang, LocKeys.BTN_DIVIDED_ORDER)}', f'{key}{user}#{LocKeys.BTN_DIVIDED_ORDER}'),
                #self._inline_btn(f'📜 {loc.get_text(lang, LocKeys.BTN_GET_FULL_ORDER)}', f'{key}{user}#{LocKeys.BTN_GET_FULL_ORDER}'),
            ],
            [
                self._inline_btn(f'📖 {loc.get_text(lang, LocKeys.BTN_MENU)}', f'{key}{user}#{LocKeys.BTN_MENU}'),
                self._inline_btn(f'🌐 {loc.get_text(lang, LocKeys.BTN_WEB)}', f'{key}{user}#{LocKeys.BTN_WEB}'),
                #self.inline_btn(loc.get_text(LocKeys.BTN_RESET_ORDER), f'{key}{user}#{LocKeys.BTN_RESET_ORDER}')
            ],
            [
                self._inline_btn(f'❎ {loc.get_text(lang, LocKeys.BTN_FINISH)}', f'{key}{user}#{LocKeys.BTN_FINISH}')
            ]
        ]

        return self._build_keyboard(keyboard)
