import logging
import credentials

from order import Order
from menu import Menu
from command import Command

from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters

class App(Updater):
    def __init__(self, token: str, logger: logging.Logger):
        super().__init__(token=token, use_context=True)
        self.log = logger
        self.info('# App init -----------')

        self.order = Order()
        self.menu = Menu(self)

        self.__create_commands()
        self.__inited = False

    def set_up(self) -> None:
        self.dispatcher.add_error_handler(lambda u, c: self.__error_handler(u, c))
        self.dispatcher.add_handler(MessageHandler(Filters.text, lambda u, c: self.__echo(u, c)))

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
    
    def __create_commands(self) -> None:
        # Probably with decorators I could get all commands instead of manually adding them
        self.__cmds = [

        ]


def main():
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    logger = logging.getLogger(__name__)

    app = App(credentials.TOKEN, logger)
    app.set_up()
    app.run()

if __name__ == '__main__':
    main()