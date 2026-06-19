import datetime
import time

def current_datetime():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

def date_difference(date1, date2):
    d1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
    d2 = datetime.datetime.strptime(date2, "%Y-%m-%d")
    return abs((d2 - d1).days)

def format_date(date, format_string):
    d = datetime.datetime.strptime(date, "%Y-%m-%d")
    return d.strftime(format_string)

def stopwatch(seconds):
    for i in range(seconds):
        print(f"Elapsed: {i+1} sec")
        time.sleep(1)

def countdown(seconds):
    for i in range(seconds, 0, -1):
        print(f"Countdown: {i}")
        time.sleep(1)
    print("Time's up!")