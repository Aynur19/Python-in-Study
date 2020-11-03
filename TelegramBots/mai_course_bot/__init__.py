# region Imports
# Подключение модулей и библиотек сторонних.
from modules.class_timetable_bot import ClassTimetableBot

from modules.invert_echo_bot import InvertEchoBot
from telegram.ext import Updater

# Подключение модулей и библиотек текущего проекта
from modules.echo_bot import EchoBot
from .log import logger
from .config import Config
# endregion


def main():
    """
    Настройка и запуск бота.
    """
    Config.read_opts()
    updater = Updater(token = Config.TOKEN, use_context = True)
    dp = updater.dispatcher

    # mai_bot = EchoBot()
    # mai_bot = InvertEchoBot()
    mai_bot = ClassTimetableBot()

    mai_bot.command_handlers_build(dp)
    mai_bot.message_handlers_build(dp)

    updater.start_polling()
    updater.idle()
