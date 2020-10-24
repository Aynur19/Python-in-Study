from telegram.ext import MessageHandler, Filters
from modules.generic_bot import GenericBot


class EchoBot(GenericBot):
    def __init__(self):
        super(EchoBot, self).__init__()
        self.name = 'echo'
        self.cmd_name = 'echo'
        self.help_info = f'/{self.cmd_name} - повторяет введенное пользователем сообщение (включает бота)\n' \
                         f"/q_{self.cmd_name} - выключает бота '{self.name}'\n"

    def cmd_echo(self, update, context):
        if self.is_enabled:
            update.message.reply_text(update.message.text)

    def message_handlers_build(self, dispatcher):
        dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, self.cmd_echo))
