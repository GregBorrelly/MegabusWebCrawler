import megabus_request
import megabus_record
import megabus_analyze
import megabus_display
import megabus_date

#working database of prices.
week_days = {
    # outbound prices
    'outbound': {
        'monday':[25,23,25],
        'tuesday':[] ,
        'wednesday':[],
        'thursday':[],
        'friday': [],
        'saturday':[],
        'sunday':[],
    },
    'inbound':{
        'imonday' : [],
        'ituesday' : [],
        'iwednesday' :[],
        'ithursday' : [],
        'ifriday' : [],
        'isaturday' : [],
        'isunday' :[],}
    }


megabus_display.run_mainSpider()
#origin = input('From: ')
#destination = input('Destination: ')
crawling = megabus_date.Date()
crawling_date, crawling_day = crawling.format_date(), crawling.day_of_the_week()
url = megabus_request.format('New York, ny', 'Boston, MA', crawling_date)


# Displays a summary of the trip that is being searched
#2megabus.params_message(html)

daysSpan = 90


# collect data
for number in range(0,daysSpan):
    print(crawling)
    if crawling_date == -1:
        crawling.increment_month()
        daysSpan = daysSpan + 1
        continue
    outbound = megabus_record.record_trips(url, 'outbound', crawling_day, week_days)
    inbound = megabus_record.record_trips(url,'inbound', crawling_day, week_days)
    crawling.increment_day()
    crawling_day = c
    rawling.day_of_the_week()

# Resets dates to compare data
crawling = megabus_date.Date()
crawling_day = crawling.day_of_the_week()
daysSpan = 90

for number in range(0,daysSpan):
    if crawling_date == None:
        crawling.increment_month()
        daysSpan = daysSpan + 1
        continue
    outbound = megabus_analyze.compare_trip_prices(url, 'outbound', crawling_day, week_days)
    inbound = megabus_analyze.compare_trip_prices(url,'inbound', crawling_day, week_days)
    crawling.increment_day()
    crawling_day = crawling.day_of_the_week()



print(week_days)


# Display
# Request information
# Records information
# Rads information
# Analyze information