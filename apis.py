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
	url = "https://iatacodes.org/api/v6/countries?api_key=" + iata_key + "&code=" + iata
    country = json.loads(requests.get(url).contant)["response"][0]['name']
    return country
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
