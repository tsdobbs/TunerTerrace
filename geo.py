import requests
import json
import os

"""
Prints top 5 most populous cities within 75 miles of a given location
Only returns cities with a population > 100k.
Using as a (maybe bad?) heuristic for if a city has a radio station.
Requires API key: https://rapidapi.com/wirefreethought/api/geodb-cities/endpoints
"""

#setting this up to read from a file for now
with open('secrets.txt','r') as file:
    key_from_file = file.read()
os.environ['API_KEY'] = key_from_file

API_KEY = os.environ['API_KEY']

API_URL = "https://wft-geo-db.p.rapidapi.com/v1/geo/cities"

def standardize_data(cities):
    """
    Some arbitrary rules to make sure that the geo api matches the radio api locations
    """
    #none yet
    return cities

def get_city_list(location, minPop =100):
    querystring = {"limit":"5",
                   "minPopulation":minPop,
                   "types":"CITY",
                   "location":location,
                   "radius":"75",
                   "distanceUnit":"MI",
                   "sort":"-population"
                  }

    headers = {
        'x-rapidapi-key': API_KEY,
        'x-rapidapi-host': "wft-geo-db.p.rapidapi.com"
        }

    response = requests.request("GET",
                                "https://wft-geo-db.p.rapidapi.com/v1/geo/cities",
                                headers=headers,
                                params=querystring
                               )

    try:
        cities = json.loads(response.text)['data']
    except:
        print(response)
    if len(cities) == 0 and minPop > 100: cities = get_city_list(location, minPop=100)
    
    cities = standardize_data(cities)

    return cities

def test_city_api():
    #LA: '+34.0522-118.2437'
    #Adelaide: '-34.9285+138.6007'
    #Windsor Locks, CT: '+41.9288-72.6481'
    #Maharashtra Region, India: '+20.3404+76.9532'
    #Buenos Aires, Argentina: '-34.5984-58.5746'
    location = '+41.9288-72.6481'

    cities = get_city_list(location)

    for city in cities:
        print(city)