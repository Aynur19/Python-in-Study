from telegram.ext import MessageHandler, Filters
from modules.generic_bot import GenericBot


class InvertEchoBot(GenericBot):
    def __init__(self):
        super(InvertEchoBot, self).__init__()
        self.name = 'invert_echo'
        self.cmd_name = 'invecho'
        self.help_info = f'/{self.cmd_name} - инвертирует введенное пользователем сообщение\n' \
                         f'/q_{self.cmd_name}- выключает бота {self.name}\n'

    def cmd_invert_echo(self, update, context):
        update.message.reply_text(update.message.text[::-1])

    def message_handlers_build(self, dispatcher):
        dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, self.cmd_invert_echo))
