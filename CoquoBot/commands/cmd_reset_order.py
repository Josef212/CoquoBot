from command import Command
from loc_keys import LocKeys

from telegram import Update

class CmdResetOrder(Command):
    def __init__(self, app):
        super().__init__(app)
        self.name = ["reset"]
    
    def execute(self, update: Update, ctx) -> None:
        chat_id = self._get_chat_id()
        self.app.reset_order(chat_id)

        lang = self._get_user_lang()
        msg = self.app.localization.get_text(lang, LocKeys.ORDER_RESET_DONE)

        self._reply_message(msg)