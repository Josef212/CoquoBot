from command import Command
from loc_keys import LocKeys

from telegram import Update

class CmdStart(Command):
    def __init__(self, app):
        super().__init__(app)
        self.name = ["start"]

    def execute(self, update: Update, ctx) -> None:
        lang = update.message.from_user.language_code
        msg = self.app.localiztion.get_text(lang, LocKeys.START_MSG)
        update.message.reply_text(msg)