from amadeus import Flights
from key import amadeus_key
from key import instagram_key

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
if __name__ == "__main__":
	for x in range(len(resp['results'])):
		destinations.append(resp['results'][x]['destination'])

	print destinations