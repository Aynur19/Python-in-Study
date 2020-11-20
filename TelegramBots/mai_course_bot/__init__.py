from time import sleep

from modules.class_timetable_bot import ClassTimetableBot

from modules.invert_echo_bot import InvertEchoBot
from telegram.ext import Updater, CommandHandler, Job
from .log import logger
from .config import Config


def daily_job(bot, update, job_queue):
    """ Running on Mon, Tue, Wed, Thu, Fri = tuple(range(5)) """
    bot.send_message(text='Setting a daily notifications!')
    job_queue.run_repeating(notify_assignees, 5, context=update)

def notify_assignees(bot, job):
    bot.send_message(text="Some text!")


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

    # updater.job_queue.start()
    # try:
    #     updater.job_queue.run_repeating(mai_bot.notify_assignees, 5)
    #     sleep(20)
    # finally:
    #     updater.stop()
    # updater.dispatcher.add_handler(CommandHandler('notify', daily_job, pass_job_queue=True))

    updater.start_polling()
    updater.idle()
