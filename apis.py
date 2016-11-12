from amadeus import Flights
from key import amadeus_key

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
