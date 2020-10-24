# region Imports
# Подключение модулей и библиотек сторонних.
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

    echo = EchoBot()
    echo.command_handlers_build(dp)
    echo.message_handlers_build(dp)

    # mai_bot = MaiCourseBot()
    #
    # echo = EchoBot()
    # echo.is_enabled = True
    # mai_bot.add_bot(echo)
    #
    # invert_echo = InvertEchoBot()
    # mai_bot.add_bot(invert_echo)
    #
    # class_timetable = ClassTimetableBot()
    # mai_bot.add_bot(class_timetable)
    #
    # mai_bot.command_handlers_build(dp)
    # mai_bot.message_handlers_build(dp)
    #
    # dp.add_handler(MessageHandler(Filters.text & ~Filters.command, mai_bot.cmd_msg_handlers_manager))

    updater.start_polling()
    updater.idle()
