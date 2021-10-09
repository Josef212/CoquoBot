import os
import logging
import credentials

from telegram.ext import Updater, MessageHandler, Filters

class App(Updater):
    def __init__(self, token: str, logger: logging.Logger):
        super().__init__(token=token, use_context=True)
        self.log = logger
        self.info('# App init')

    def set_up(self):
        self.dispatcher.add_error_handler(lambda u, c: self.__error_handler(u, c))
        self.dispatcher.add_handler(MessageHandler(Filters.text, lambda u, c: self.__echo(u, c)))

    def run(self):
        self.start_polling()
        self.idle()

    def info(self, msg: str):
        self.log.info(msg)
    
    def warn(self, msg: str):
        self.log.warning(msg)

    def error(self, msg: str):
        self.log.error(msg)

    def __error_handler(self, update, ctx):
        self.warn(f'Update {update.message.text} caused error:\n  {ctx.error}')
    
    def __echo(self, update, ctx):
        update.message.reply_text(update.message.text)


def main():
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    logger = logging.getLogger(__name__)

    app = App(credentials.TOKEN, logger)
    app.set_up()
    app.run()

if __name__ == '__main__':
    main()