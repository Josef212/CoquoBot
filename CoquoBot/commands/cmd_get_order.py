from command import Command
from loc_keys import LocKeys

from telegram import Update

class CmdGetOrderBase(Command):
    def __init__(self, app):
        super().__init__(app)

    def format_order(self, order: dict, title: str, lang: str) -> str:
        cart = order['cart']
        price = order['total']

        loc = self.app.localization
        menu = self.app.menu

        missing_any_price = False
        msg = f'{title}\n'

        for item in cart:
            amount = cart[item]
            item_price = menu.get_item_price(item)
            msg += f'  - {amount}x {item}. ({item_price}€ / 1)\n'
        
            if item_price == 0.0:
                missing_any_price = True
        
        if missing_any_price:
            missing_text = loc.get_text(lang, LocKeys.GET_ORDER_MISSING_PRICE)
            msg += f'\n {missing_text}\n'
        
        total_price_text = loc.get_text(lang, LocKeys.GET_ORDER_TOTAL_PRICE)
        msg += f'\n{total_price_text}: {price}€'

        return msg
    
    def get_full_order_text(self, chat_id: int, lang: str) -> str:
        full_order = self.app.get_full_order(chat_id)
        title = self.app.localization.get_text(lang, LocKeys.GET_ORDER_TITLE_FULL_ORDER)
        return self.format_order(full_order, title, lang)

    def get_user_order_text(self, chat_id: int, user: str, lang: str) -> str:
        user_order = self.app.get_user_order(chat_id, user)
        title = self.app.localization.get_text_format(lang, LocKeys.GET_ORDER_TITLE_GET_USERS, user)
        return self.format_order(user_order, title, lang)
    
class CmdGetOrderFor(CmdGetOrderBase):
    def __init__(self, app):
        super().__init__(app)
        self.name = ["get_order_for"]

    def execute(self, update: Update, ctx) -> None:
        loc = self.app.localization
        lang = self._get_user_lang()

        args = update.message.text.split()
        arg_count = len(args)

        if arg_count < 2:
            text = loc.get_text(lang, LocKeys.GET_ORDER_MISSING_ARGS)
            self._reply_message(text)
            return

        if arg_count > 2:
            text = loc.get_text(lang, LocKeys.GET_ORDER_TOO_MUCH_ARGS)
            self._reply_message(text)
            return

        user = args[1] # TODO: Maybe need to remove start_with(@)
        chat_id = self._get_chat_id()

        msg = self.get_user_order_text(chat_id, user, lang)
        self._send_message(msg)

class CmdGetMyOrder(CmdGetOrderBase):
    def __init__(self, app):
        super().__init__(app)
        self.name = ["get_my_order"]
    
    def execute(self, update: Update, ctx) -> None:
        chat_id = self._get_chat_id()
        user = self._get_username()
        lang = self._get_user_lang()

        msg = self.get_user_order_text(chat_id, user, lang)
        self._send_message(msg)

class CmdGetFullOrder(CmdGetOrderBase):
    def __init__(self, app):
        super().__init__(app)
        self.name = ["get_full_order"]
    
    def execute(self, update: Update, ctx) -> None:
        chat_id = self._get_chat_id()
        lang = self._get_user_lang()

        msg = self.get_full_order_text(chat_id, lang)
        self._send_message(msg)
