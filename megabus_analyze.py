import megabus_record
import megabus_request


def compare_trip_prices(url, mode, crawling_day, week_days):
    """Sorts through each row of data """
    id = 0  # numerical number used to display current trip.
    while True:
        # Downloads HTML using URL, gets all availible trips.
        megabus_trip = megabus_request.download_trips(url, id, mode)

        if megabus_trip == []:  # An empty list mea m ns we reached the end of the road.
            break

        # Selects the Trip based on ID provided before in download_trips, ID is
        # passed once more but only to be able to print the currebt trip number.
        for data_row in megabus_trip:
            data = megabus_request.Trip(data_row, id, mode, crawling_day)
            price = data.price(verbose=False)
            price_list = megabus_record.get_price_list(mode, crawling_day, week_days)
            average_price = find_average(price_list)
            print('Trip Price ', price,'Average Price ', average_price)
        id = id + 1

def find_average(list):
    temp = 0
    for price in list:
        temp = temp + price
    average = temp/len(list)
    return average
def plot(week_Days):
    monday_prices = week_Days['outbound']['monday']
    tuesday_prices = week_Days['outbound']['tuesday']
    wednesday_prices = week_Days['outbound']['wednesday']
    thursday_prices = week_Days['outbound']['thursday']
    friday_prices = week_Days['outbound']['friday']
    saturday_prices = week_Days['outbound']['saturday']
    sunday_prices = week_Days['outbound']['sunday']

    plt.plot(monday_prices, label="Monday")
    plt.plot(tuesday_prices, label='Tuesday')
    plt.plot(wednesday_prices, label='Wednesday')
    plt.plot(thursday_prices, label="Thursday")
    plt.plot(friday_prices, label='Friday')
    plt.plot(saturday_prices, label='Saturday')
    plt.plot(sunday_prices, label='Sunday')
    plt.legend(loc='upper left')
    plt.show()

def send_results():
    pass