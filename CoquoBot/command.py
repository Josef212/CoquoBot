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
            self.cmd = CommandHandler(self.name, lambda u, c: self.execute(u, c))
        
        return self.cmd
    
    @abc.abstractmethod
    def execute(self, update: Update, ctx) -> None:
        pass

    def get_help(self):
        return f'{self.name}: {self.name}'
    
    def get_username_from_update(self, update: Update) -> str:
        return update.message.from_user.username
    
    def get_username_from_query(self, query: CallbackQuery) -> str:
        return query.from_user.username

    def get_user_lang_from_update(self, update: Update) -> str:
        return update.message.from_user.language_code
    
    def get_user_lang_from_query(self, query: CallbackQuery) -> str:
        return query.from_user.language_code
    
    def get_chat_id(self, ctx) -> int:
        return ctx.message.chat.id
    
    def update_reply_message(self, update: Update, msg: str, markup=None) -> None:
        update.message.reply_text(msg, reply_markup=markup)

    def query_reply_message(self, query: CallbackQuery, msg: str, markup=None) -> None:
        query.message.reply_text(msg, reply_markup=markup)
    
    def query_edit_message(self, query: CallbackQuery, msg: str, markup=None) -> None:
        query.edit_message_text(msg, reply_markup=markup)
    
    def get_inline_btn_args_from_query(self, query) -> list:
        return query.data.split('#')

    def inline_btn(self, text: str, cbk_data: str = ''):
        return { 'text': text, 'callback_data': cbk_data }

    def build_keyboard(self, keyboard: list):
        return json.dumps({ 'inline_keyboard': keyboard })

# Command implementation example
class TestCmd(Command):
    def __init__(self, app):
        super().__init__(app)
        self.name = ["TestCmd", "proves"]

    def execute(self, update, ctx):
        update.message.reply_text(f'Executing [{self.name}] command')

    def get_help(self):
        return f'{self.name}: A simple test command that displays a basic text.'
