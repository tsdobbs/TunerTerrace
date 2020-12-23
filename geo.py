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

url = "https://wft-geo-db.p.rapidapi.com/v1/geo/cities"

#LA: '+34.0522-118.2437'
#Adelaide: '-34.9285+138.6007'
#Windsor Locks, CT: '+41.9288-72.6481'
location = '+41.9288-72.6481'

querystring = {"limit":"5","minPopulation":"100000","types":"CITY","location":location,"radius":"75","distanceUnit":"MI"}

headers = {
    'x-rapidapi-key': API_KEY,
    'x-rapidapi-host': "wft-geo-db.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

cities = json.loads(response.text)['data']

for city in cities:
    print(city)