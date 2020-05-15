import datetime
from django.utils import timezone
from datetime import timedelta



def get_today_start():
    """
    :return: Start Date (YYYY-MM-DD HH:MM:SS): 2016-03-1 00:00:00
    """
    return timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)


def get_today_end():
    """
    :return: End Date (YYYY-MM-DD HH:MM:SS): 2016-03-15 23:59:59
    """
    tomorrow = get_today_start() + timedelta(days=1)
    return tomorrow - timedelta(microseconds=1)



def get_day_start(date):
    """
    :return: Start Date (YYYY-MM-DD HH:MM:SS): 2016-03-1 00:00:00
    """

    date_time = datetime.datetime.combine(date, datetime.time.min)
    return date_time.replace(hour=0, minute=0, second=0, microsecond=0)


def get_day_end(date):
    """
    :return: End Date (YYYY-MM-DD HH:MM:SS): 2016-03-15 23:59:59
    """
    date_time = datetime.datetime.combine(date, datetime.time.min)
    return date_time.replace(hour=23, minute=59, second=59, microsecond=0)
