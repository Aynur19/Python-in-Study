from datetime import datetime


class ClassTimetable:
    weekday: str
    lessonStart: datetime
    lessonEnd: datetime
    lessonName: str
    teacherName: str
    isEveryWeek: bool
    isEvenWeek: bool
    isOddWeek: bool
    isOnceMonth: bool
    isOnline: bool
    otherInfo: str

    def __init__(self, weekday: str = '', lesson_start: datetime = datetime.now(), lesson_end: datetime = datetime.now(),
                 lesson_name: str = '', teacher_name: str = '', is_every_week: bool = True,
                 is_even_week: bool = True, is_odd_week: bool = True, is_once_month: bool = False,
                 is_online: bool = True, other_info: str = ''):

        self.weekday = weekday
        self.lessonStart = lesson_start
        self.lessonEnd = lesson_end
        self.lessonName = lesson_name
        self.teacherName = teacher_name
        self.isEveryWeek = is_every_week
        self.isEvenWeek = is_even_week
        self.isOddWeek = is_odd_week
        self.isOnceMonth = is_once_month
        self.isOnline = is_online
        self.otherInfo = other_info
