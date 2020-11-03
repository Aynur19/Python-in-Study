from datetime import datetime
from nameof import nameof


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

    def __init__(self, weekday: str, lesson_start: datetime, lesson_end: datetime,
                 lesson_name: str, teacher_name: str, is_every_week: bool,
                 is_even_week: bool, is_odd_week: bool, is_once_month: bool,
                 is_online: bool, other_info: str, data: {}):
        if data is not None:
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

    def data_parsing(self, data: {}):
        fieldnames =[nameof(self.weekday), nameof(self.lessonStart), nameof(self.lesson_end), nameof(self.lesson_name),
                     nameof(self.teacher_name), nameof(self.is_every_week), nameof(self.is_even_week),
                     nameof(self.is_odd_week), nameof(self.is_once_month), nameof(self.is_online), nameof(self.other_info)]
        check = all(field in data.keys for field in fieldnames)

        if check is True:
            self.weekday = data[nameof(self.weekday)]
            self.lessonStart = data[nameof(self.lessonStart)]
            self.lessonEnd = data[nameof(self.lessonEnd)]
            self.lessonName = data[nameof(self.lessonName)]
            self.teacherName = data[nameof(self.teacherName)]
            self.isEveryWeek = data[nameof(self.isEveryWeek)]
            self.isEvenWeek = data[nameof(self.isEvenWeek)]
            self.isOddWeek = data[nameof(self.isOddWeek)]
            self.isOnceMonth = data[nameof(self.isOnceMonth)]
            self.isOnline = data[nameof(self.isOnline)]
            self.otherInfo = data[nameof(self.otherInfo)]
