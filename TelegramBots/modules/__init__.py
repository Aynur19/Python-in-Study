from telegram.ext import CommandHandler


class GenericBot:
    name: str
    cmd_name: str
    help_info: str
    is_enabled: bool

    def __init__(self):
        self.is_enabled = False

    def cmd_help(self, update, context):
        update.message.reply_text(self.help_info)

    def cmd_start(self, update, context):
        if not self.is_enabled:
            self.is_enabled = True
            update.message.reply_text(f'Бот \'{self.name}\' включен!')

    def cmd_stop(self, update, context):
        if self.is_enabled:
            self.is_enabled = False
            update.message.reply_text(f'Бот \'{self.name}\' выключен!')

    def command_handlers_build(self, dispatcher):
        dispatcher.add_handler(CommandHandler(f'help', self.cmd_help))
        dispatcher.add_handler(CommandHandler(f'{self.cmd_name}', self.cmd_start))
        dispatcher.add_handler(CommandHandler(f'q_{self.cmd_name}', self.cmd_stop))

    def message_handlers_build(self, dispatcher):
        pass