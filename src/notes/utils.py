from datetime import datetime


def datetime_now():
    """ Correct time """
    now = datetime.now()
    date = now.strftime('%d.%m.%Y %H:%M:%S')
    return date
