from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import csv
import datetime

from modules.generic_bot import GenericBot


class ClassTimetableBot(GenericBot):

    def __init__(self):
        super().__init__()
        self.name = 'class_timetable'
        self.cmd_name = 'ct'
        self.bot_info = f'/{self.cmd_name} - бот для работы с расписанием занятий\n'
        self.help_info = f'/{self.cmd_name} - включение бота работы с расписанием\n' \
                         f'/ct_days - вывод дней недели\n' \
                         f'/q_{self.cmd_name} - выключение бота {self.name}\n' \
                         f'\n'
        self.week_days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    #
    # def cmd_timetable_days(self, update, context):
    #     """
    #     Бот 'class_timetable'. Вывод кнопок для выбора дня недели
    #     :param update: - событие получения сообщения от пользователя.
    #     :param context: - текущее состояние бота.
    #     """
    #     if self.is_enabled:
    #         buttons = [[InlineKeyboardButton(self.week_days[0], callback_data=self.week_days[0]),
    #                     InlineKeyboardButton(self.week_days[1], callback_data=self.week_days[1])],
    #                    [InlineKeyboardButton(self.week_days[2], callback_data=self.week_days[2]),
    #                     InlineKeyboardButton(self.week_days[3], callback_data=self.week_days[3])],
    #                    [InlineKeyboardButton(self.week_days[4], callback_data=self.week_days[4]),
    #                     InlineKeyboardButton(self.week_days[5], callback_data=self.week_days[5])]]
    #
    #         reply_markup = InlineKeyboardMarkup(buttons)
    #         update.message.reply_text('Выбери день:', reply_markup=reply_markup)
    #
    # def button(self, update, context):
    #     query = update.callback_query
    #     query.answer()
    #
    #     #query.edit_message_text(text="Selected option: {}".format(query.data))
    #
    # def command_handlers_build(self, dispatcher):
    #     """
    #     Построение обработчиков событий получения от пользователя сообщений с командами.
    #     :param dispatcher: - диспетчер обработчиков событий телеграм-бота.
    #     """
    #     dispatcher.add_handler(CommandHandler("ct_days", self.work))
    #     dispatcher.add_handler(CallbackQueryHandler(self.button))
    #
    # def message_handlers_build(self, dispatcher):
    #     """
    #     Построение обработчиков событий получения от пользователя обычных сообщений.
    #     :param dispatcher: - диспетчер обработчиков событий телеграм-бота.
    #     """
    #     pass
