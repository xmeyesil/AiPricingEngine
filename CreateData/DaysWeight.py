from datetime import date

class DaysWeight:

    def __init__(self, day):
        if (type(day) == date):
            self.day = day.weekday()
        else:
            self.day = day


    def dayWeight(self):

        days = {
            0: 1.1,
            1: 1,
            2: 1,
            3: 1.1,
            4: 1.2,
            5: 1.5,
            6: 1.2
        }

        return days[self.day]

