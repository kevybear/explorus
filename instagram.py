from instagram_lib.client import InstagramAPI
from apis import *

class InstagramLib():
	def __init__(self):
		tokenfile = open('token.txt','r')
		self.token = str(tokenfile.read())
		secretfile = open('secret.txt','r')
		self.secret = str(secretfile.read())
	
	def get_client(self):
		api = InstagramAPI(access_token=self.token, client_secret=self.secret)
		return api

	def get_photos_from_location(self, latitude, longitude, count):
		api = self.get_client()
		loc = api.location_search(lng=longitude, lat=latitude, count=count)
		recent_media, next_ = api.location_recent_media(location_id = loc[0].id)
		return recent_media

	def get_photos_user(self, username):
		user_id = api.user_search(username)[0].id
		recent_media, next_ = api.user_recent_media(user_id=user_id, count=10)
		return recent_media

	def check_keys(self):
		print(self.token)
		print(self.secret)

def getPhotos(city):
	instagram = InstagramLib()
	locations = getPointsCoors(city)
	names = getPointsNames(city)
	lis = []
	for x in range(4):
		lat = locations[x][0]
		lon = locations[x][1]
		name = names[x]
		photo = instagram.get_photos_from_location(lat, lon, 1)
		if photo:
			url = photo[0].get_standard_resolution_url()
			lis.append((name, url))
		else: 
			continue
	return lis
