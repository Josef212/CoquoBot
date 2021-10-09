from command import Command
from loc_keys import LocKeys

from telegram import Update

class CmdStart(Command):
    def __init__(self, app):
        super().__init__(app)
        self.name = ["start"]

    def execute(self, update: Update, ctx) -> None:
        lang = self.get_user_lang_from_update(update)
        msg = self.app.localiztion.get_text(lang, LocKeys.START_MSG)
        self.reply_message(update, msg)