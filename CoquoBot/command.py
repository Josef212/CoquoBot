import abc
from telegram.ext import CommandHandler

class Command(metaclass=abc.ABCMeta):
    def __init__(self, app):
        self.app = app
        self.name = "unasigned"
        self.cmd = None

    def get_command(self):
        if self.cmd == None:
            self.cmd = CommandHandler(self.name, lambda u, c: self.execute(u, c))
        
        return self.cmd
    
    @abc.abstractmethod
    def execute(self, update, ctx):
        pass

    def get_help(self):
        return f'{self.name}: {self.name}'

# Command implementation example
class TestCmd(Command):
    def __init__(self, app):
        super().__init__(app)
        self.name = ["TestCmd", "proves"]

    def execute(self, update, ctx):
        update.message.reply_text(f'Executing [{self.name}] command')

    def get_help(self):
        return f'{self.name}: A simple test command that displays a basic text.'
