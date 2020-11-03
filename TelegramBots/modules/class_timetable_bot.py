import csv

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, CallbackQueryHandler

from modules import GenericBot


class ClassTimetableBot(GenericBot):

    def __init__(self):
        super().__init__()
        self.name = 'class_timetable'
        self.cmd_name = 'ct'
        self.help_info = f'/{self.cmd_name} - включение бота работы с расписанием занятий\n' \
                         f'/ct_days - вывод дней недели\n' \
                         f'/q_{self.cmd_name} - выключение бота {self.name}\n'
        self.week_days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']

    def cmd_timetable_days(self, update, context):
        """
        Бот 'class_timetable'. Вывод кнопок для выбора дня недели
        :param update: - событие получения сообщения от пользователя.
        :param context: - текущее состояние бота.
        """
        if self.is_enabled:
            buttons = [[InlineKeyboardButton(self.week_days[0], callback_data=self.week_days[0]),
                        InlineKeyboardButton(self.week_days[1], callback_data=self.week_days[1])],
                       [InlineKeyboardButton(self.week_days[2], callback_data=self.week_days[2]),
                        InlineKeyboardButton(self.week_days[3], callback_data=self.week_days[3])],
                       [InlineKeyboardButton(self.week_days[4], callback_data=self.week_days[4]),
                        InlineKeyboardButton(self.week_days[5], callback_data=self.week_days[5])]]

            reply_markup = InlineKeyboardMarkup(buttons)
            update.message.reply_text('Выбери день:', reply_markup=reply_markup)

    def button(self, update, context):
        query = update.callback_query
        query.answer()

        ct_dict = {}
        # with open('./data/ClassTimetable.csv', 'r', encoding='utf-8') as csv_file:
        #     reader = csv.reader(csv_file, delimiter="\n")
        #     for row, line in enumerate(reader):
        #         for column in [s.split(';') for s in line][row]:
        #             if i == 0:
        #                 ct_dict.update({column: ''})
        #             else:
        #                 ct_dict.update({ct_dict.})
        #         print(f'line[{0}] = {1}'.format(i, line))
        #query.edit_message_text(text="Selected option: {}".format(query.data))

    def command_handlers_build(self, dispatcher):
        """
        Построение обработчиков событий получения от пользователя сообщений с командами.
        :param dispatcher: - диспетчер обработчиков событий телеграм-бота.
        """
        super(ClassTimetableBot, self).command_handlers_build(dispatcher)
        dispatcher.add_handler(CommandHandler("ct_days", self.cmd_timetable_days))
        dispatcher.add_handler(CallbackQueryHandler(self.button))
