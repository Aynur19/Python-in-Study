# region Imports
# Подключение модулей и библиотек сторонних.
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

    # echo = EchoBot()
    # echo.command_handlers_build(dp)
    # echo.message_handlers_build(dp)

    invert_echo = InvertEchoBot()
    invert_echo.command_handlers_build(dp)
    invert_echo.message_handlers_build(dp)

    updater.start_polling()
    updater.idle()
