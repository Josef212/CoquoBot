from command import Command

from telegram import Update

class CmdWeb(Command):
    def __init__(self, app):
        super().__init__(app)
        self.name = ["web"]
    
    def execute(self, update: Update, ctx) -> None:
        url = self.app.menu.get_menu_web()
        self._send_message(url)

class CmdMenu(Command):
    def __init__(self, app):
        super().__init__(app)
        self.name = ["menu"]
    
    def execute(self, update: Update, ctx) -> None:
        msg = self.get_menu_text()
        self._send_message(msg)

    def get_menu_text(self) -> str:
        # TODO: Could localize the menu
        menu = self.app.menu
        menu_list = menu.get_menu_list()

        msg = f'COQUO menu:\n'
        for item in menu_list:
            item_price = menu.get_item_price(item)
            msg += f'  - {item}: {item_price}€\n'
        
        return msg
