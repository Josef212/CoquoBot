from command import Command
from loc_keys import LocKeys

from telegram import Update

class CmdHelp(Command):
    def __init__(self, app):
        super().__init__(app)
        self.name = ["help", "ajuda", "ayuda"]
    
    def execute(self, update: Update, ctx) -> None:
        pass