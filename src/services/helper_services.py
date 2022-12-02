from datetime import datetime

class DateHelper(object):

    bulgarian_days = [
      'понеделник',
      'вторник',
      'сряда',
      'четвъртък',
      'петък',
      'събота',
      'неделя'
    ]

    @staticmethod
    def get_day():
        return datetime.today().weekday()
    
    @classmethod
    def get_day_in_bulgarian(cls):
        day = cls.get_day()
        return cls.bulgarian_days[day].capitalize()
