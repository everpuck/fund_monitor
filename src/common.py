# author everpuck


import time
import datetime
import smtplib


def transaction_time():
    # check_time = ['14:00:00', '14:55:00',]
    check_time = ['20:00:00', '23:55:00',]
    day_of_week = datetime.datetime.now().weekday()
    print(day_of_week)
    # dayOfWeek = datetime.today().weekday()
    begin = datetime.datetime.now().strftime("%Y-%m-%d") + ' ' + check_time[0]
    end = datetime.datetime.now().strftime("%Y-%m-%d") + ' ' + check_time[1]
    begin_seconds=time.time()-time.mktime(time.strptime(begin, '%Y-%m-%d %H:%M:%S'))
    end_seconds=time.time()-time.mktime(time.strptime(end, '%Y-%m-%d %H:%M:%S'))
    if (int(day_of_week) in range(7)) and \
        int(begin_seconds) > 0 and int(end_seconds) < 0:
        return 1
    else:
        return 0


def send_email():
    pass


def test():
    print(transaction_time())


if __name__ == "__main__":
    test()
