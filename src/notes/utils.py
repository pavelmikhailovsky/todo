from datetime import datetime, timezone


def datetime_now():
    now = datetime.now()
    date = now.strftime('%d.%m.%Y %H:%M:%S')
    return date
