import datetime

def time_var():
    return datetime.datetime.now().strftime("%H:%M")

def date_var():
    return datetime.date.today().strftime("%Y-%m-%d")