from amadeus import Flights
from key import *
import requests
from flask import *
import json

# ============================  Functions ===========================================

def convertToCity(iata):
	url = "https://iatacodes.org/api/v6/airports?api_key=" + iata_key + "&code=" + iata
	city = json.loads(requests.get(url).content)["response"][0]['name']
	return city

def cityToCountry(iata):
	country_code_url = "https://iatacodes.org/api/v6/airports?api_key=" + iata_key + "&code=" + iata
	country_code = json.loads(requests.get(country_code_url).content)["response"][0]["country_code"]
	url = "https://iatacodes.org/api/v6/countries?api_key=" + iata_key + "&code=" + country_code
	country = json.loads(requests.get(url).content)['response'][0]['name']
	return country

"""def cityToIATA(city):
	city_code_url = "https://iatacodes.org/api/v6/airports?api_key=" + iata_key + "&code=" + city
	city_code = json.loads(requests.get(city_code_url).content)["response"][0]["city_code"]
	url = "https://iatacodes.org/api/v6/cities?api_key=" + iata_key + "&code" + city_code
	iata = json.loads(requests.get(url).content)
	return iata"""

def cityToLatLong(city):
	

# =============================== Scripts ==========================================

flights = Flights(amadeus_key)
origin = 'BKK'
departure_date = None
price = None
duration = None
direct = None
aggregation_mode = None

resp = flights.inspiration_search(
    origin=origin,
    departure_date=departure_date,
    max_price=price,
    duration=duration,
    direct=direct,
    aggregation_mode=aggregation_mode)



destinations = []

prices = []
for x in range(len(resp['results'])):
	destinations.append(resp['results'][x]['destination'])
	prices.append(resp['results'][x]['price'])

print(destinations[0])
print(cityToCountry(destinations[0]))
