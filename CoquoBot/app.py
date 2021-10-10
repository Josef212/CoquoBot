import logging
import credentials

from order import Order
from order_manager import OrderManager
from menu import Menu
from localization import Localization

from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters

from commands.cmd_start import *
from commands.cmd_coquo import *
from commands.cmd_menu import *

class App(Updater):
    def __init__(self, token: str, logger: logging.Logger):
        super().__init__(token=token, use_context=True)
        self.log = logger
        self.info('# App init -----------')

        self.__order_manager = OrderManager()
        self.menu = Menu(self)
        self.localization = Localization()

        self.__create_commands()
        self.__inited = False

    def set_up(self) -> None:
        self.dispatcher.add_error_handler(lambda u, c: self.__error_handler(u, c))
        #self.dispatcher.add_handler(MessageHandler(Filters.text, lambda u, c: self.__echo(u, c)))

        for cmd in self.__cmds:
            self.dispatcher.add_handler(cmd.get_command())
        
        self.__inited = True

    def run(self) -> None:
        self.start_polling()
        self.idle()

    def add_command(self, cmd: Command) -> None:
        self.__cmds.append(cmd)
        if self.__inited:
            self.dispatcher.add_handler(cmd.get_command())

    def info(self, msg: str) -> None:
        self.log.info(msg)
    
    def warn(self, msg: str) -> None:
        self.log.warning(msg)

    def error(self, msg: str) -> None:
        self.log.error(msg)

    def __error_handler(self, update: Update, ctx) -> None:
        self.warn(f'Update {update.message.text} caused error:\n  {ctx.error}')
    
    def __echo(self, update: Update, ctx):
        update.message.reply_text(update.message.text)
    
    def get_order(self, chat_id: int) -> Order:
        return self.__order_manager.get_order(chat_id)
    
    def reset_order(self, chat_id: int) -> None:
        self.__order_manager.reset_order(chat_id)

    def add_to_order(self, chat_id: int, user: str, item: str, amount: int) -> None:
        self.__order_manager.get_order(chat_id).add_to_order(user, item, amount)
    
    def get_user_order(self, chat_id: int, user: str) -> dict:
        return self.__order_manager.get_order(chat_id).get_user_order(user)
    
    def get_full_order(self, chat_id: int) -> dict:
        return self.__order_manager.get_order(chat_id).get_full_order()
    
    def get_all_commands(self) -> list:
        return self.__cmds
    
    def get_command(self, cmd_name: str) -> Command:
        for cmd in self.__cmds:
            if cmd.name == cmd_name or cmd_name in cmd.name:
                return cmd
            
        return None
    
    def __create_commands(self) -> None:
        # Probably with decorators I could get all commands instead of manually adding them
        self.__cmds = [
            CmdStart(self),
            CmdCoquo(self),
            CmdWeb(self),
            CmdMenu(self),
        ]


def main():
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    logger = logging.getLogger(__name__)

    app = App(credentials.TOKEN, logger)
    app.set_up()
    app.run()

if __name__ == '__main__':
    main()