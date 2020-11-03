from datetime import datetime
from models import ClassTimetable
import csv


def write_class_timetable():
    header, data = get_class_timetable_data()

    with open('../data/ClassTimetable.csv', 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=';')
        csv_writer.writerow(header)

        for lesson in data:
            csv_writer.writerow([f'{lesson.weekday}',
                                 f'{lesson.lesson_start}',
                                 f'{lesson.lesson_end}',
                                 f'{lesson.lesson_name}',
                                 f'{lesson.teacher_name}',
                                 f'{lesson.is_every_week}',
                                 f'{lesson.is_even_week}',
                                 f'{lesson.is_odd_week}',
                                 f'{lesson.is_once_month}',
                                 f'{lesson.is_online}',
                                 f'{lesson.other_info}',
                                 ])


def get_class_timetable_data():
    header = ['weekday', 'lessonStart', 'lessonEnd', 'lessonName',
              'teacherName', 'isEveryWeek', 'isEvenWeek', 'isOddWeek',
              'isOnceMonth', 'isOnline', 'otherInfo']

    data = []
    data.append(ClassTimetable('Понедельник',
                               datetime.strptime('18:15', '%H:%M'),
                               datetime.strptime('21:30', '%H:%M'),
                               'Основы методов обработки и анализа данных',
                               'Джумурат А. С.',
                               other_info='YouTube'))

    data.append(ClassTimetable('Вторник',
                               datetime.strptime('18:15', '%H:%M'),
                               datetime.strptime('21:30', '%H:%M'),
                               'Фундаментальные концепции ИИ',
                               'Кондаратцев В. Л.',
                               other_info='Zoom'))

    data.append(ClassTimetable('Среда',
                               datetime.strptime('09:00', '%H:%M'),
                               datetime.strptime('11:00', '%H:%M'),
                               'Unity',
                               'Лушников А. Ю.',
                               is_even_week=True,
                               is_odd_week=False,
                               is_every_week=False,
                               other_info='Zoom'))

    data.append(ClassTimetable('Среда',
                               datetime.strptime('18:00', '%H:%M'),
                               datetime.strptime('20:00', '%H:%M'),
                               'Unity',
                               'Лушников А. Ю.',
                               is_every_week=False,
                               is_even_week=False,
                               is_odd_week=True,
                               other_info='Zoom'))

    data.append(ClassTimetable('Среда',
                               datetime.strptime('18:15', '%H:%M'),
                               datetime.strptime('21:30', '%H:%M'),
                               'Английский язык',
                               'Осадчая С. В,',
                               is_every_week=False,
                               is_even_week=True,
                               is_odd_week=False,
                               other_info='Zoom'))

    data.append(ClassTimetable('Четверг',
                               datetime.strptime('16:00', '%H:%M'),
                               datetime.strptime('17:30', '%H:%M'),
                               'Мониторинг проектной деятельности',
                               'IT-центр, науч. рук.',
                               is_odd_week=False,
                               is_even_week=False,
                               is_every_week=False,
                               is_once_month=True,
                               other_info='Zoom'))

    data.append(ClassTimetable('Четверг',
                               datetime.strptime('18:15', '%H:%M'),
                               datetime.strptime('21:30', '%H:%M'),
                               'Программная инженерия',
                               'Рыбалко А.',
                               other_info='Zoom'))

    data.append(ClassTimetable('Суббота',
                               datetime.strptime('09:00', '%H:%M'),
                               datetime.strptime('12:15', '%H:%M'),
                               'Agile',
                               'Вяткин П. М.',
                               other_info='Zoom'))

    data.append(ClassTimetable('Суббота',
                               datetime.strptime('12:30', '%H:%M'),
                               datetime.strptime('15:30', '%H:%M'),
                               'Python',
                               'Иванов А. Н.',
                               other_info='Zoom'))

    return header, data


def filtration_class_timetable(predicate):
    reader = csv.DictReader(open(r"../data/ClassTimetable.csv", 'r', encoding='utf-8'), delimiter=';')
    rows = filter_dict(reader, predicate)
    print(rows)


def filter_dict(csv_reader: csv.DictReader, callback):
    list_of_dict = []
    for line in csv_reader:
        if callback(line):
            list_of_dict.append(line)

    return list_of_dict


if __name__ == '__main__':
    # write_class_timetable()
    filtration_class_timetable(predicate=lambda x: x['weekday'] == 'Среда')