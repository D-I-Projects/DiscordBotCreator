import datetime

class BotVariables:

    @staticmethod
    def time_var():
        return datetime.datetime.now().strftime("%H:%M")

    @staticmethod
    def date_var():
        return datetime.date.today().strftime("%Y-%m-%d")
