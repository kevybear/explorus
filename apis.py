from amadeus import Flights
from key import *
import requests
from flask import *
import json
iata_key = 'SFO'

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

	
def getPointsCoors(city):
	url = "https://api.sandbox.amadeus.com/v1.2/points-of-interest/yapq-search-text?city_name=" + city + "&apikey=" + amadeus_key
	request = json.loads(requests.get(url).content)
	pois = request['points_of_interest']
	coors = []
	for site in pois:
		location = site['location']
		lats = location['latitude']
		longi = location['longitude']
		coors.append([lats, longi])
	return coors


def getPointsNames(city):
	url = "https://api.sandbox.amadeus.com/v1.2/points-of-interest/yapq-search-text?city_name=" + city + "&apikey=" + amadeus_key
	request = json.loads(requests.get(url).content)
	pois = request['points_of_interest']
	titles = []
	for site in pois:
		names = site['title']
		titles.append(names)
	return titles
# =============================== Scripts ==========================================

flights = Flights(amadeus_key)
origin = 'BKK'
departure_date = None
price = None
duration = None
direct = None
aggregation_mode = None

# resp = flights.inspiration_search(
#     origin=origin,
#     departure_date=departure_date,
#     max_price=price,
#     duration=duration,
#     direct=direct,
#     aggregation_mode=aggregation_mode)



# destinations = []

# prices = []
# for x in range(len(resp['results'])):
# 	destinations.append(resp['results'][x]['destination'])
# 	prices.append(resp['results'][x]['price'])
