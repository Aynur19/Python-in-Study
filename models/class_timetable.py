import datetime


class ClassTimetable:
    weekday: str
    lesson_start: datetime
    lesson_end: datetime
    lesson_name: str
    teacher_name: str
    is_every_week: bool
    is_even_week: bool
    is_odd_week: bool
    is_once_month: bool
    is_online: bool
    other_info: str

    def __init__(self, weekday: str, lesson_start: datetime, lesson_end: datetime,
                 lesson_name: str, teacher_name: str, is_every_week: bool = True,
                 is_even_week: bool = True, is_odd_week: bool = True, is_once_month: bool = False,
                 is_online: bool = True, other_info: str = ''):
        self.weekday = weekday
        self.lesson_start = lesson_start
        self.lesson_end = lesson_end
        self.lesson_name = lesson_name
        self.teacher_name = teacher_name
        self.is_every_week = is_every_week
        self.is_even_week = is_even_week
        self.is_odd_week = is_odd_week
        self.is_once_month = is_once_month
        self.is_online = is_online
        self.other_info = other_info

