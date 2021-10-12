import abc
import json

from telegram import Update, CallbackQuery, Message
from telegram.ext import CommandHandler

class Command(metaclass=abc.ABCMeta):
    def __init__(self, app):
        self.app = app
        self.name = "unasigned"
        self.cmd = None

    def get_command(self) -> CommandHandler:
        if self.cmd == None:
            self.cmd = CommandHandler(self.name, lambda u, c: self.do_execute(u, c))
        
        return self.cmd
    
    def do_execute(self, update: Update, ctx) -> None:
        self.__update = update
        self.__ctx = ctx
        self.execute(update, ctx)
    
    @abc.abstractmethod
    def execute(self, update: Update, ctx) -> None:
        pass

    def get_help(self):
        return f'{self.name}: {self.name}'
    
    def _set_cmd_data(self, update: Update, ctx) -> None:
        self.__update = update
        self.__ctx = ctx
    
    def _get_effective_message(self) -> Message:
        # TODO: Could use effective_message. This is none for inline_cbk and some more cases but would do the trick as this one
        query = self.__update.callback_query
        return self.__update.message if query == None else query.message
    
    def _get_username(self) -> str:
        query = self.__update.callback_query
        return self.__update.message.from_user.username if query == None else query.from_user.username
    
    def _get_user_lang(self) -> str:
        query = self.__update.callback_query
        return self.__update.message.from_user.language_code if query == None else query.from_user.language_code

    def _get_chat_id(self) -> int:
        return self._get_effective_message().chat.id
    
    def _send_message(self, msg: str, markup=None) -> Message:
        chat_id = self._get_chat_id()
        return self.app.bot.send_message(chat_id, msg, reply_markup=markup)
    
    def _reply_message(self, msg: str, markup=None) -> None:
        self._get_effective_message().reply_text(msg, reply_markup=markup)
    
    def _query_edit_message(self, query: CallbackQuery, msg: str, markup=None) -> None:
        query.edit_message_text(msg, reply_markup=markup)
    
    def _get_inline_btn_args_from_query(self, query: CallbackQuery) -> list:
        return query.data.split('#')

    def _inline_btn(self, text: str, cbk_data: str = ''):
        return { 'text': text, 'callback_data': cbk_data }

    def _build_keyboard(self, keyboard: list):
        return json.dumps({ 'inline_keyboard': keyboard })
    
    def _execute_command(self, cmd_name: str) -> None:
        cmd = self.app.get_command(cmd_name)
        if cmd == None:
            self.app.error(f'Could not find command named: {cmd_name}')
            return

        cmd.do_execute(self.__update, self.__ctx)

# Command implementation example
class TestCmd(Command):
    def __init__(self, app):
        super().__init__(app)
        self.name = ["TestCmd", "proves"]

    def execute(self, update, ctx):
        self._reply_message(f'Executing [{self.name}] command')

    def get_help(self):
        return f'{self.name}: A simple test command that displays a basic text.'
