import megabus_request

def record_price_to_list( mode, crawling_day, trip_price, week_days):
    """Records the provided price to list."""
    # crawling_day is used to determined to which list of days the price has to be appendend too.
    # Mode is used to determined wherever this is a inbound or outbound trip.
    day = crawling_day.lower()
    mode = mode

    if mode == 'outbound':
        week_days[mode][day].append(trip_price)

    if mode == 'inbound':
        day = 'i' + day
        week_days[mode][day].append(trip_price)


def get_price_list(mode, crawling_day, week_days):
    mode = mode
    day = crawling_day.lower()

    if mode == 'outbound':
        return week_days[mode][day]

    if mode == 'inbound':
        day = 'i' + day
        return week_days[mode][day]


def record_trips(url, mode,crawling_day, week_days):
    """Sorts through each row of data """
    id = 0  # numerical number used to display current trip.
    print("\nDownloading {0}'s".format(crawling_day), mode,'Data')
    #progress_bar(1.00)

    while True:
        #Downloads HTML using URL, gets all availible trips.
        megabus_trip = megabus_request.download_trips(url, id, mode)
        if megabus_trip == []:  # An empty list means we reached the end of the road.
            break

        # Selects the Trip based on ID provided before in download_trips, ID is
        # passed once more but only to be able to print the currebt trip number.
        for data_row in megabus_trip:
            data = megabus_request.Trip(data_row, id, mode, crawling_day)
            price = data.price(verbose=False)
            record_price_to_list(mode, crawling_day, price, week_days)
        id += 1

