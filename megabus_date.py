import datetime

class Date():
    def __init__(self):
        self.today = datetime.datetime.today()
        self.year = int(self.today.strftime('%y')) + 2000
        self.month = int(self.today.strftime('%m'))
        self.day = int(self.today.strftime('%d'))

    def format_date(self):
        try:
            date = datetime.datetime(self.year,self.month,self.day)
            formatted_Date = date.strftime('%m/%d/%y')
            return formatted_Date

        except ValueError:
            print('New Month')
            return -1



    def increment_day(self):
        self.day =self.day + 1

    def increment_month(self):
        self.month = self.month + 1
        self.day = 1

    def day_of_the_week(self):
        date = datetime.datetime(self.year,self.month,self.day)
        day = date.strftime('%A')
        return day

# Tests

#crawling_date = Date(2016, 4, 25)

#crawling_date.increment_day()
#crawling_date.day_of_the_week()
#print(crawling_date.format_date())

