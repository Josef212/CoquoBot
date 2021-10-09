import abc

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
    def execute(self, update, ctx) -> None:
        pass

    def get_help(self):
        return f'{self.name}: {self.name}'
    
    def get_username_from_update(self, update) -> str:
        return update.message.from_user.user_name

    def get_user_lang_from_update(self, update) -> str:
        return update.message.from_user.language_code
    
    def get_chat_id_from_update(self, update) -> int:
        return update.message.chat.id
    
    def reply_message(self, update, msg: str) -> None:
        update.message.reply_text(msg)
    
    def edit_message(self, query, msg: str) -> None:
        query.message.edit_message_text(msg)

# Command implementation example
class TestCmd(Command):
    def __init__(self, app):
        super().__init__(app)
        self.name = ["TestCmd", "proves"]

    def execute(self, update, ctx):
        update.message.reply_text(f'Executing [{self.name}] command')

    def get_help(self):
        return f'{self.name}: A simple test command that displays a basic text.'
