import sys, os
import logging

from order import Order
from order_manager import OrderManager
from menu import Menu
from localization import Localization

from telegram import Update
from telegram.ext import Updater, CallbackContext, MessageHandler, Filters

from commands.cmd_start import *
from commands.cmd_coquo import *
from commands.cmd_menu import *
from commands.cmd_reset_order import *
from commands.cmd_get_order import *
from commands.cmd_order import *
from commands.cmd_edit_order import *
from commands.cmd_add_order import *
from commands.cmd_help import *
from commands.cmd_info import *

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

    def __error_handler(self, update: Update, ctx: CallbackContext) -> None:
        self.warn(f'Update {update.message.text} caused error:\n  {ctx.error}')
    
    def __echo(self, update: Update, ctx):
        update.message.reply_text(update.message.text)
    
    def get_order(self, chat_id: int) -> Order:
        return self.__order_manager.get_order(chat_id)
    
    def reset_order(self, chat_id: int) -> None:
        self.__order_manager.reset_order(chat_id)

    def add_to_order(self, chat_id: int, user: str, item: str, amount: int) -> None:
        self.__order_manager.get_order(chat_id).add_to_order(user, item, amount)
    
    def user_has_any_order(self, chat_id: int, user: str) -> bool:
        return self.__order_manager.user_has_any_order(chat_id, user)

    def get_user_order(self, chat_id: int, user: str) -> dict:
        return self.__order_manager.get_order(chat_id).get_user_order(self.menu, user)
    
    def get_full_order(self, chat_id: int) -> dict:
        return self.__order_manager.get_order(chat_id).get_full_order(self.menu)
    
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
            CmdResetOrder(self),
            CmdGetMyOrder(self),
            CmdGetOrderFor(self),
            CmdGetFullOrder(self),
            CmdOrder(self),
            CmdEditOrder(self),
            CmdAddOrder(self),
            CmdAddOrderMe(self),
            CmdHelp(self),
            CmdInfo(self),
            CmdGetFullOrderDivided(self),
        ]


def main():
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    logger = logging.getLogger(__name__)

    token = str(os.environ.get('TELEGRAM_TOKEN', ''))

    app = App(token, logger)
    app.set_up()
    app.run()

if __name__ == '__main__':
    main()
