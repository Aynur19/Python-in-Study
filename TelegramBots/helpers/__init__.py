from datetime import datetime
from datetime import date

def is_even_week(
        actual_date: datetime = datetime.now(),
        study_start_date: datetime = None):
    if study_start_date is None:
        study_start_date = date(datetime.now().year, 9, 1)

    weeks = actual_date.isocalendar()[1] - study_start_date.isocalendar()[1] - 1
    return not weeks & 1
