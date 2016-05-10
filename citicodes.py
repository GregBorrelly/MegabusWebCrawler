""" Small Script to find citi destinations codes for MEGABUS"""

from urllib.request import urlopen
from bs4 import BeautifulSoup

number = 89 # First city. 
while True:
    try:
        url = 'http://us.megabus.com/JourneyResults.aspx?originCode={0}&destinationCode=143&outboundDepartureDate=4%2f16%2f2016&inboundDepartureDate=4%2f16%2f2016&passengerCount=2&transportType=0&concessionCount=0&nusCount=0&outboundWheelchairSeated=0&outboundOtherDisabilityCount=0&inboundWheelchairSeated=0&inboundOtherDisabilityCount=0&outboundPcaCount=0&inboundPcaCount=0&promotionCode=&withReturn=1'.format(number)
        html = urlopen(url)
        soup = BeautifulSoup(html)
        places = []
        for place in soup.findAll("strong"):# City name is in between a strong tag
            places.append(place.getText())
        print("'"+places[0].upper()+"'"+' : '+"'"+str(number)+"'"+',') # formats the city into a dictionary to be used later.
        number += 1

    except IndexError: #Some cities skip a digit or two, this code stops the indexerror from stopping the program.
        number +=1
        continue
    else:
        if number > 145: # This is the numerical code for the last city. 
            print('Done')
            break
"""" 
Sample Output :
 'ALBANY, NY' : '89',
        'AMHERST, MA' : '90',
        'ANN ARBOR, MI' : '91',
        'ATLANTIC CITY, NJ' : '92',
        'BINGHAMTON, NY' : '93',
        'BOSTON, MA' : '94',
        'BUFFALO, NY' : '95',
        'BURLINGTON, VT' : '96',
        'CAMDEN' : '97',
        'CHAMPAIGN, IL' : '98',
        'CHARLOTTE, NC' : '99',
        'CHICAGO, IL' : '100',
        'CHRISTIANSBURG, VA' : '101',
        'CINCINNATI, OH' : '102',
        'CLEVELAND, OH' : '103',
        'COLUMBIA, MO' : '104',
        'COLUMBUS, OH' : '105',
        'DES MOINES, IA' : '106',
        'DETROIT, MI' : '107',
        'ERIE, PA' : '108',
        'FREDERICK, MD' : '109',
        'HAMPTON, VA' : '110',
        'HARRISBURG, PA' : '111',
        'HARTFORD, CT' : '112',
        'HOLYOKE, CT' : '113',
        'HYANNIS, MA' : '114',
        'INDIANAPOLIS, IN' : '115',
        'IOWA CITY, IA' : '116',
        'KANSAS CITY, MO' : '117',
        'KNOXVILLE, TN' : '118',
        'MADISON, WI' : '119',
        'MEMPHIS, TN' : '120',
        'MILWAUKEE, WI' : '121',
        'NEW HAVEN, CT' : '122',
        'NEW YORK, NY' : '123',
        'NIAGARA FALLS, ON' : '124',
        'NORMAL, IL' : '125',
        'OMAHA, NE' : '126',
        'PHILADELPHIA, PA' : '127',
        'PITTSBURGH, PA' : '128',
        'PORTLAND, ME' : '129',
        'PROVIDENCE, RI' : '130',
        'DURHAM, NC' : '131',
        'RICHMOND, VA' : '132',
        'RIDGEWOOD, NJ' : '133',
        'ROCHESTER, NY' : '134',
        'SECAUCUS, NJ' : '135',
        'ST LOUIS, MO' : '136',
        'STATE COLLEGE, PA' : '137',
        'STORRS, CT' : '138',
        'SYRACUSE, NY' : '139',
        'TOLEDO, OH' : '140',

""""
