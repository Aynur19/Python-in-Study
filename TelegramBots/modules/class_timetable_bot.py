"""Бот расписания занятий"""
import datetime

import telegram
import helpers as help
from models import ClassTimetable
from nameof import nameof
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from telegram.ext import CommandHandler, CallbackQueryHandler, CallbackContext, MessageHandler, Filters
from helpers.helper_csv import filtration_class_timetable
from modules import GenericBot
from os import path
from modules import constants as const


class ClassTimetableBot(GenericBot):

    def __init__(self):
        super().__init__()
        self.name = 'class_timetable'
        self.cmd_name = 'ct'
        self.help_info = f'/{self.cmd_name} - включение бота работы с расписанием занятий\n' \
                         f'/ct_days - вывод дней недели\n' \
                         f'/q_{self.cmd_name} - выключение бота {self.name}\n'
        self.week_days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
        self.model = ClassTimetable()

    def command_handlers_build(self, dispatcher):
        """
        Построение обработчиков событий получения от пользователя сообщений с командами.
        :param dispatcher: - диспетчер обработчиков событий телеграм-бота.
        """
        super(ClassTimetableBot, self).command_handlers_build(dispatcher)
        dispatcher.add_handler(CommandHandler("start", self.get_start_menu))
        # dispatcher.add_handler(MessageHandler(Filters.regex(const.btn_start_menu_ct), self.get_class_timetable_days))
        dispatcher.add_handler(CallbackQueryHandler(self.get_ct_btns, pattern=nameof(const.btn_start_menu_ct)))
        dispatcher.add_handler(CallbackQueryHandler(self.get_ct_full, pattern=nameof(const.btn_ct_full)))
        dispatcher.add_handler(CallbackQueryHandler(self.get_ct_week, pattern=nameof(const.btn_week_)))
        dispatcher.add_handler(CallbackQueryHandler(self.get_ct_weekday_btns, pattern=nameof(const.btn_weekday)))
        dispatcher.add_handler(CallbackQueryHandler(self.get_ct_day, pattern=nameof(const.btn_day_)))
        dispatcher.add_handler(CommandHandler("set_reminder", self.set_timer, pass_args=True, pass_job_queue=True, pass_chat_data=True))

    def alarm(self, context: CallbackContext):
        """Send the alarm message."""
        job = context.job
        context.bot.send_message(job.context, text="sdfsdfsdf")

    def set_timer(self, update: telegram.Update, context: CallbackContext):
        chat_id = update.message.chat_id

        if 'job' in context.chat_data:
            old_job = context.chat_data['job']
            old_job.schedule_removal()
        new_job = context.job_queue.run_repeating(self.alarm, 5, context=chat_id)
        context.chat_data['job'] = new_job

        update.message.reply_text('Timer successfully set!')

    def get_start_menu(self, update: telegram.Update, context: CallbackContext):
        """Стартовое меню"""
        menu = [[InlineKeyboardButton(const.btn_start_menu_ct, callback_data=nameof(const.btn_start_menu_ct)),
                 InlineKeyboardButton(const.btn_start_menu_notify, callback_data=const.btn_start_menu_notify)]]
        reply_markup = InlineKeyboardMarkup(menu)
        update.message.reply_text(const.msg_start_menu, reply_markup=reply_markup)

    def get_ct_btns(self, update: telegram.Update, context: CallbackContext):
        """Меню -> Расписание занятий"""
        query = update.callback_query
        query.answer()

        menu = [[InlineKeyboardButton(const.btn_ct_full, callback_data=nameof(const.btn_ct_full)),
                 InlineKeyboardButton(const.btn_weekday, callback_data=nameof(const.btn_weekday))],
                [InlineKeyboardButton(const.btn_week_current, callback_data=nameof(const.btn_week_current)),
                 InlineKeyboardButton(const.btn_week_next, callback_data=nameof(const.btn_week_next))],
                [InlineKeyboardButton(const.btn_day_today, callback_data=nameof(const.btn_day_today)),
                 InlineKeyboardButton(const.btn_day_tomorrow, callback_data=nameof(const.btn_day_tomorrow))]]

        reply_markup = InlineKeyboardMarkup(menu)
        query.edit_message_text(text=const.msg_ct, reply_markup=reply_markup)

    def get_ct_weekday_btns(self, update: telegram.Update, context: CallbackContext):
        """Меню -> Расписание -> День недели"""
        query = update.callback_query
        query.answer()

        menu = [[InlineKeyboardButton(const.btn_day_mon, callback_data=nameof(const.btn_day_mon)),
                 InlineKeyboardButton(const.btn_day_tue, callback_data=nameof(const.btn_day_tue))],
                [InlineKeyboardButton(const.btn_day_wed, callback_data=nameof(const.btn_day_wed)),
                 InlineKeyboardButton(const.btn_day_thu, callback_data=nameof(const.btn_day_thu))],
                [InlineKeyboardButton(const.btn_day_fri, callback_data=nameof(const.btn_day_fri)),
                 InlineKeyboardButton(const.btn_day_sat, callback_data=nameof(const.btn_day_sat))]]

        reply_markup = InlineKeyboardMarkup(menu)
        query.edit_message_text(text=const.msg_day_btns, reply_markup=reply_markup)

    def get_ct(self, predicate):
        filepath = path.join(path.dirname(path.dirname(__file__)), const.file_path_class_timetable)
        ct_dict = filtration_class_timetable(filepath, predicate=predicate)
        return ct_dict

    def get_ct_full(self, update: telegram.Update, context: CallbackContext):
        """Меню -> Расписание -> Полное"""
        query = update.callback_query
        query.answer()

        ct_dict = self.get_ct(lambda x: x is not None)
        answer_message = ''
        for line in ct_dict:
            answer_message += self.add_ct_answer_delimiter()
            answer_message += self.add_ct_answer_generic(line)
            answer_message += self.add_ct_answer_week(line)
            answer_message += self.add_ct_answer_other_info(line)

        answer_message += self.add_ct_answer_delimiter()
        query.edit_message_text(text=answer_message)

    def get_ct_week(self, update: telegram.Update, context: CallbackContext):
        """
        Меню -> Расписание -> Эта неделя
        Меню -> Расписание -> След. неделя
        """
        query = update.callback_query
        query.answer()

        query_data = query.data

        if query_data == nameof(const.btn_week_current):
            is_even_week = help.is_even_week()
            ct_dict = self.get_ct(lambda x: x[nameof(self.model.isEvenWeek)] == f'{is_even_week}')
        elif query_data == nameof(const.btn_week_next):
            is_even_week = not help.is_even_week()
            ct_dict = self.get_ct(lambda x: x[nameof(self.model.isOddWeek)] != f'{is_even_week}')

        answer_message = f''
        for line in ct_dict:
            answer_message += self.add_ct_answer_delimiter()
            answer_message += self.add_ct_answer_generic(line)
            answer_message += self.add_ct_answer_other_info(line)

        answer_message += self.add_ct_answer_delimiter()
        query.edit_message_text(text=answer_message)

    def get_weekday(self, query_data: str):
        """Получение значения дня недели по кнопке"""
        if query_data == nameof(const.btn_day_today):
            return datetime.datetime.today().weekday()
        elif query_data == nameof(const.btn_day_tomorrow):
            return (datetime.datetime.today() + datetime.timedelta(days=1)).weekday()
        elif query_data == nameof(const.btn_day_mon):
            return 0
        elif query_data == nameof(const.btn_day_tue):
            return 1
        elif query_data == nameof(const.btn_day_wed):
            return 2
        elif query_data == nameof(const.btn_day_thu):
            return 3
        elif query_data == nameof(const.btn_day_fri):
            return 4
        elif query_data == nameof(const.btn_day_sat):
            return 5
        elif query_data == nameof(const.btn_day_sun):
            return 6

    def get_ct_day(self, update: telegram.Update, context: CallbackContext):
        """
        Меню -> Респисание -> Сегодня
        Меню -> Расписание -> Завтра
        Меню -> Расписание -> День недели -> День
        """
        query = update.callback_query
        query.answer()

        query_data = query.data

        weekday = self.get_weekday(query_data)
        if weekday == 0:
            weekday_str = const.btn_day_mon
        elif weekday == 1:
            weekday_str = const.btn_day_tue
        elif weekday == 2:
            weekday_str = const.btn_day_wed
        elif weekday == 3:
            weekday_str = const.btn_day_thu
        elif weekday == 4:
            weekday_str = const.btn_day_fri
        elif weekday == 5:
            weekday_str = const.btn_day_sat
        elif weekday == 6:
            weekday_str = const.btn_day_sun
        else:
            weekday_str = None

        ct_dict = self.get_ct(lambda x: (x[nameof(self.model.weekday)] == weekday_str))

        answer_message = f''
        if len(ct_dict) <= 0:
            answer_message += self.add_ct_answer_delimiter()
            if query_data == nameof(const.btn_day_today):
                answer_message += self.add_ct_answer_not_in_day(const.btn_day_today)
            elif query_data == nameof(const.btn_day_tomorrow):
                answer_message += self.add_ct_answer_not_in_day(const.btn_day_tomorrow)
            else:
                answer_message += self.add_ct_answer_not_in_day(weekday_str)
        else:
            for line in ct_dict:
                answer_message += self.add_ct_answer_delimiter()
                answer_message += self.add_ct_answer_generic(line)
                answer_message += self.add_ct_answer_other_info(line)

        answer_message += self.add_ct_answer_delimiter()
        query.edit_message_text(text=answer_message)

    # region Add Class Timetable Answer
    def add_ct_answer_delimiter(self):
        """Добавление в ответ разделителя занятий"""
        return f'{const.msg_ct_delimiter}\n'

    def add_ct_answer_generic(self, ct_dict_line: {}):
        """Добавление в ответ основной информации по занятию"""
        answer_message = f'{const.msg_ct_weekday} {ct_dict_line[nameof(self.model.weekday)]}\n' \
                         f'{const.msg_ct_lesson_start} {ct_dict_line[nameof(self.model.lessonStart)][slice(-8, -3)]}\n' \
                         f'{const.msg_ct_lesson_end} {ct_dict_line[nameof(self.model.lessonEnd)][slice(-8, -3)]}\n' \
                         f'{const.msg_ct_lesson_name} {ct_dict_line[nameof(self.model.lessonName)]}\n' \
                         f'{const.msg_ct_teacher_name} {ct_dict_line[nameof(self.model.teacherName)]}\n'

        return answer_message

    def add_ct_answer_week(self, ct_dict_line: {}):
        """Добавление занятии о неделе"""
        if ct_dict_line[nameof(self.model.isEveryWeek)]:
            return f'{const.msg_ct_is_every_w}\n'
        elif ct_dict_line[nameof(self.model.isEvenWeek)]:
            return f'{const.msg_ct_is_even_w}\n'
        elif ct_dict_line[nameof(self.model.isOddWeek)]:
            return f'{const.msg_ct_is_odd_w}\n'
        elif ct_dict_line[nameof(self.model.isOnceMonth)]:
            return f'{const.msg_ct_is_once_month}\n'
        else:
            return f''

    def add_ct_answer_other_info(self, ct_dict_line: {}):
        """Добавлении остальной информации о занятии"""
        answer_message = f''
        if ct_dict_line[nameof(self.model.isOnline)]:
            answer_message += f'{const.msg_ct_is_online}\n'
        else:
            answer_message += f'{const.msg_ct_is_offline}\n'

        if ct_dict_line[nameof(self.model.otherInfo)] is not None:
            answer_message += f'{const.msg_ct_other_info} {ct_dict_line[nameof(self.model.otherInfo)]}\n'

        return answer_message

    def add_ct_answer_not_in_day(self, weekday: str):
        return f'{weekday}: {const.msg_ct_not}\n'
    # endregion


