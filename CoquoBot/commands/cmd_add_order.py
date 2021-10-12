from command import Command
from loc_keys import LocKeys

from telegram import Update

class CmdAddOrder(Command):
    def __init__(self, app):
        super().__init__(app)
        self.name = ["add_order"]
    
    def execute(self, update: Update, ctx) -> None:
        loc = self.app.localization
        lang = self._get_user_lang()
        chat_id = self._get_chat_id()

        if update.callback_query != None:
            return

        args = update.message.text.split()
        if len(args) <= 2:
            text = loc.get_text(lang, LocKeys.ADD_ORDER_MISSING_ARGS)
            self._reply_message(text)
            return
        
        user = args[1]
        if user[0] == '@':
            user = user[1:]
        
        msg = loc.get_text_format(lang, LocKeys.ADD_ORDER_ITEMS_ADDED, user)
        items = args[2:]
        for item in items:
            self.app.add_to_order(chat_id, user, item, 1)

            text = self.app.localization.get_text_format(lang, LocKeys.ORDER_ITEM_ADDED, item)
            msg += f'\n  - {text}'
        
        self._send_message(msg)

class CmdAddOrderMe(Command):
    def __init__(self, app):
        super().__init__(app)
        self.name = ["add_order_me"]
    
    def execute(self, update: Update, ctx) -> None:
        loc = self.app.localization
        lang = self._get_user_lang()
        chat_id = self._get_chat_id()
        user = self._get_username()

        if update.callback_query != None:
            return

        args = update.message.text.split()
        if len(args) <= 1:
            text = loc.get_text(lang, LocKeys.ADD_ORDER_ME_MISSING_ARGS)
            self._reply_message(text)
            return
        
        msg = loc.get_text_format(lang, LocKeys.ADD_ORDER_ITEMS_ADDED, user)
        items = args[1:]
        for item in items:
            self.app.add_to_order(chat_id, user, item, 1)

            text = self.app.localization.get_text_format(lang, LocKeys.ORDER_ITEM_ADDED, item)
            msg += f'\n  - {text}'
        
        self._send_message(msg)
