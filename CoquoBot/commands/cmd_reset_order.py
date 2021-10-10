from command import Command
from loc_keys import LocKeys

from telegram import Update

class CmdResetOrder(Command):
    def __init__(self, app):
        super().__init__(app)
        self.name = ["reset"]
    
    def execute(self, update: Update, ctx) -> None:
        chat_id = self.get_chat_id(update)
        self.app.reset_order(chat_id)

        lang = self.get_user_lang_from_update(update)
        msg = self.app.localization.get_text(lang, LocKeys.ORDER_RESET_DONE)

        self.update_reply_message(update, msg)