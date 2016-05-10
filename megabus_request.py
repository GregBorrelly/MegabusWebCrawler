import webtools
import re

class Trip():
    """ Models a megabus trip."""

    def __init__(self, data, number, mode, crawling_day):
        """ Initializes basic trip Data."""
        self.data = data
        self.trip_number = number
        self.mode = mode
        self.day = crawling_day

    def price(self, verbose=True):
        """
        Returns the price of the trip, and prints the price if verbose is set to True
        :return: price = int
        """
        data = self.data
        price_regex = re.compile(r"\$\d\d")  # Dollard Sign followed by two digits.
        matches = price_regex.findall(data)
        price = matches[0]
        if verbose == True:
            print('Price: ', price)
        price = price.replace('$', '')  # Cleans up data, so it can be converted to int easier later.
        return int(price)

    def departure_time(self):
        """Gets & Prints the departure time, :Returns: departure_time = str """
        data = self.data
        departure_regex = re.compile(r"^(Departs\d+:\d\d...)")  # DepartsDigitormore, :, two more digits
        matches = departure_regex.findall(data)
        departure_time = matches[0]
        departure_time = departure_time.replace('Departs', '')
        print('Departing: ', departure_time)
        return departure_time

    def arrival_time(self):
        """Gets & Prints the arrival time, :Returns: arrival_time = str """
        data = self.data
        arrival_regex = re.compile(r"(Arrives\d+:\d\d...)")
        matches = arrival_regex.findall(data)
        arrival_time = matches[0]
        arrival_time = arrival_time.replace('Arrives', '')
        print('Arriving: ', arrival_time)
        return arrival_time

    def display_trip(self):
        """ Displays some of the current trip attributes. """
        print('\n')
        if self.mode == 'inbound':
            print(' Outbound Trip {0} '.center(50, '=').format(self.trip_number + 1))
        if self.mode == 'outbound':
            print(' Inbound Trip {0} '.center(50, '=').format(self.trip_number + 1))

        self.price()
        self.departure_time()
        self.arrival_time()


def generate_city_code(citi):
    """
    A dictionary of city codes used by megabus to identify each city.
    :return: The proper city code, string.
    """
    citi = citi.strip() # Strips the city provided of any extra spaces
    citi = citi.upper()
    citi_codes = {
        'ALBANY, NY': '89',
        'AMHERST, MA': '90',
        'ANN ARBOR, MI': '91',
        'ATLANTIC CITY, NJ': '92',
        'BINGHAMTON, NY': '93',
        'BOSTON, MA': '94',
        'BUFFALO, NY': '95',
        'BURLINGTON, VT': '96',
        'CAMDEN': '97',
        'CHAMPAIGN, IL': '98',
        'CHARLOTTE, NC': '99',
        'CHICAGO, IL': '100',
        'CHRISTIANSBURG, VA': '101',
        'CINCINNATI, OH': '102',
        'CLEVELAND, OH': '103',
        'COLUMBIA, MO': '104',
        'COLUMBUS, OH': '105',
        'DES MOINES, IA': '106',
        'DETROIT, MI': '107',
        'ERIE, PA': '108',
        'FREDERICK, MD': '109',
        'HAMPTON, VA': '110',
        'HARRISBURG, PA': '111',
        'HARTFORD, CT': '112',
        'HOLYOKE, CT': '113',
        'HYANNIS, MA': '114',
        'INDIANAPOLIS, IN': '115',
        'IOWA CITY, IA': '116',
        'KANSAS CITY, MO': '117',
        'KNOXVILLE, TN': '118',
        'MADISON, WI': '119',
        'MEMPHIS, TN': '120',
        'MILWAUKEE, WI': '121',
        'NEW HAVEN, CT': '122',
        'NEW YORK, NY': '123',
        'NIAGARA FALLS, ON': '124',
        'NORMAL, IL': '125',
        'OMAHA, NE': '126',
        'PHILADELPHIA, PA': '127',
        'PITTSBURGH, PA': '128',
        'PORTLAND, ME': '129',
        'PROVIDENCE, RI': '130',
        'DURHAM, NC': '131',
        'RICHMOND, VA': '132',
        'RIDGEWOOD, NJ': '133',
        'ROCHESTER, NY': '134',
        'SECAUCUS, NJ': '135',
        'ST LOUIS, MO': '136',
        'STATE COLLEGE, PA': '137',
        'STORRS, CT': '138',
        'SYRACUSE, NY': '139',
        'TOLEDO, OH': '140',
    }
    return citi_codes[citi] # Returns the city code to be formatted into an URL.


def generate_date(date):
    """
    Formats the provided date, returns: String
    """
    date = date
    date = date.replace('/', '\n')
    date = date.split()
    month, day, year = date[0], date[1], date[2]
    date = month + '%2f' + day + '%2f' + year
    return date


def format(origin, destination, crawling_date, passengers='2'):
    """ Formats a Megabus URL with the destination information."""
    base = 'http://us.megabus.com/JourneyResults.aspx?'
    origincode = 'originCode=' + generate_city_code(origin)
    destinationcode = '&destinationCode=' + generate_city_code(destination)   # Crawling date is provided twice
    departuredate = '&outboundDepartureDate=' + generate_date(crawling_date) # This is done to get both outgoing
    coming_back = '&inboundDepartureDate=' + generate_date(crawling_date)   # and ingoing trips with the same URL
    passengers = '&passengerCount=' + passengers
    rest_of_url = '&transportType=0&concessionCount=0&nusCount=0&outboundWheelchairSeated=0&outboundOtherDisabilityCount=0&inboundWheelchairSeated=0&inboundOtherDisabilityCount=0&outboundPcaCount=0&inboundPcaCount=0&promotionCode=&withReturn=1'
    url = base + origincode + destinationcode + departuredate + coming_back + passengers + rest_of_url
    return url



def params_message(soup):
    """ prints a consise message of the search being done """
    soup = soup
    message = []
    # The message is stored under tag div, in class "search_params"
    print('|SEARCHING FOR TRIP TO|')
    for word in soup.findAll('div', {"class": "search_params"}):
        message.append(word.getText())

    for word in message:
        # Removes tabs and space.
        word = word.replace('\t', '')
        word = word.replace('\n', '')
        print(word)

def format_trip_id(number, mode):
    """formats the ID to be search with the numerical id(number)"""
    # This functions returns the link to be used to search for trips.
    # mode refers to whereever the trip is inbound or outbound.
    # This function is equipped to deal with both
    # incoming trips and outgoing trips.
    # ID is converted from int to str to be able to concantanate with url.
    if mode == 'inbound':
        if number > 9:
            # If ID is a two digit number, it formats the last two digits.
            number = str(number)
            id = 'JourneyResylts_InboundList_GridViewResults_ctl07_row_item'
            id = id.replace('07', number)
            return id
        else:
            # If Id is a one digit number, it formats the last digit only.
            number = str(number)
            id = 'JourneyResylts_InboundList_GridViewResults_ctl07_row_item'
            id = id.replace('7', number)
            return id # returns the formatted ID to be used to search for trips

    if mode == 'outbound':
        if number > 9:
            number = str(number)
            id = 'JourneyResylts_OutboundList_GridViewResults_ctl09_row_item'
            id = id.replace('09', number)
            return id
        else:
            number = str(number)
            id = 'JourneyResylts_OutboundList_GridViewResults_ctl09_row_item'
            id = id.replace('9', number)
            return id
    else:
        print("Something is wrong with Mode")


def download_trips(url, id, mode):
    """Returns a string with the trip information """
    identification = format_trip_id(id, mode)
    html = webtools.DownloadData(url)
    temp = []
    trip = []
    for trip_data in html.findAll('ul', id=identification):
        temp.append(trip_data.getText())
    for word in temp:
        word = word.replace('\t', '')
        word = word.replace('\n', '')
        word = word.replace('\r', '')
        trip.append(word)
    return trip

