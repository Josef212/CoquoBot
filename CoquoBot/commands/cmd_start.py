from command import Command
from loc_keys import LocKeys

from telegram import Update

class CmdStart(Command):
    def __init__(self, app):
        super().__init__(app)
        self.name = ["start"]

    def execute(self, update: Update, ctx) -> None:
        lang = self._get_user_lang()
        msg = self.app.localization.get_text(lang, LocKeys.START_MSG)

        self._reply_message(msg)