from telegram.ext import Updater, CommandHandler
from modules.generic_bot import GenericBot


class MaiCourseBot(GenericBot):
    bots: {}
    current_bot: GenericBot

    # def __init__(self):
    #     super(MaiCourseBot, self).__init__()
    #     self.name = 'mai_course'
    #     self.cmd_name = 'mai'
    #     self.bot_info = f"/{self.cmd_name} - главный бот\n"
    #     self.help_info = "/start - начало беседы нового пользователя с ботом\n" \
    #                      "/help - вывод списка команд с описаниями\n" \
    #                      "/bots - вывод списка ботов с описаниями\n" \
    #                      "\n"
    #     self.is_enabled = True
    #     self.bots = {}
    #     self.current_bot = None
    #
    # def add_bot(self, bot: GenericBot):
    #     self.bots.update({bot.cmd_name: bot})
    #     # self.help_info += bot.help_info
    #     self.bot_info += bot.bot_info
    #
    #     if bot.is_enabled:
    #         if self.current_bot is not None:
    #             self.bots[self.current_bot.cmd_name].is_enabled = False
    #         self.current_bot = bot
    #
    # def cmd_start(self, update, context):
    #     update.message.reply_text(f"Привет, {update.message.chat.username}! Ты начал общение с '{self.name}'!")
    #
    # def cmd_help(self, update, context):
    #     update.message.reply_text(self.help_info)
    #
    # def cmd_bots(self, update, context):
    #     update.message.reply_text(self.bot_info)
    #
    # def cmd_start_bot(self, update, context):
    #     cmd = update.message.text
    #     cmd = cmd[1:]
    #     if cmd in self.bots:
    #         if self.current_bot is None:
    #             self.current_bot = self.bots[cmd]
    #         update.message.reply_text(self.start_bot(self.bots[cmd]))
    #     else:
    #         update.message.reply_text(f'Указанного бота не существует!')
    #
    # def cmd_stop_bot(self, update, context):
    #     cmd = update.message.text
    #     cmd = cmd[3:]
    #     if self.current_bot is None:
    #         self.current_bot = self.bots[cmd]
    #     update.message.reply_text(self.stop_bot(cmd))
    #
    # def start_bot(self, new_bot: GenericBot):
    #     if new_bot.cmd_name == self.current_bot.cmd_name:
    #         return f"Бот '{self.current_bot.name}' уже запущен"
    #     else:
    #         new_bot.is_enabled = True
    #         self.current_bot = new_bot
    #         return f"Начал работу бот '{self.current_bot.name}'!"
    #
    # def stop_bot(self, bot_name: str):
    #     if self.current_bot.cmd_name != bot_name:
    #         return f"Бот '{bot_name}' уже не работает!"
    #     elif not self.current_bot.is_enabled:
    #         return f"Бот '{self.current_bot.name}' уже не работает!"
    #     else:
    #         self.current_bot.is_enabled = False
    #         return f"Бот '{self.current_bot.name}' прекратил работу!"
    #
    # def command_handlers_build(self, dispatcher):
    #     dispatcher.add_handler(CommandHandler('start', self.cmd_start))
    #     dispatcher.add_handler(CommandHandler('help', self.cmd_help))
    #     dispatcher.add_handler(CommandHandler('bots', self.cmd_bots))
    #
    #     for key in self.bots:
    #         dispatcher.add_handler(CommandHandler(f'{key}', self.cmd_start_bot))
    #         dispatcher.add_handler(CommandHandler(f'q_{key}', self.cmd_stop_bot))
    #         self.bots[key].command_handlers_build(dispatcher)
    #         self.bots[key].message_handlers_build(dispatcher)
    #
    # def cmd_msg_handlers_manager(self, update, context):
    #     if (self.current_bot is not None) and self.current_bot.is_enabled:
    #         if self.current_bot.cmd_name == 'invecho':
    #             self.bots['invecho'].cmd_invert_echo(update, context)
    #         elif self.current_bot.name == 'echo':
    #             self.bots['echo'].cmd_echo(update, context)
    #
    # def message_handlers_build(self, dispatcher):
    #     pass
