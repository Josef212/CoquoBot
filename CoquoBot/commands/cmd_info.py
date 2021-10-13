from command import Command
from loc_keys import LocKeys

from telegram import Update

TELF = '+34 605 73 60 09'
DIR = 'C/ Bisbe Messeguer 12 25003 Lleida'
EMAIL = 'pizzacoquo@gmail.com'

class CmdInfo(Command):
    def __init__(self, app):
        super().__init__(app)
        self.name = ["info"]
    
    def execute(self, update: Update, ctx) -> None:
        lang = self._get_user_lang()

        msg = f'COQUO info:\n'
        msg += f'  - Telf.: {TELF}\n'
        msg += f'  - Dir.: {DIR}\n'
        msg += f'  - @: {EMAIL}\n'
        msg += f'  - {self.app.localization.get_text(lang, LocKeys.INFO_SCHEDULE)}'

        self._send_message(msg)