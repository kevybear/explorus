from instagram_lib.client import InstagramAPI

"""
Account: annielin143
Access token:
(u'387829024.a9a03de.832693a120bc4da183e39c982f030a8c', 
{u'username': u'annielin143', u'bio': u'', u'website': u'',
 u'profile_picture': u'https://scontent.cdninstagram.com/
 t51.2885-19/s150x150/12383630_1651519118433084_1091366395_a.jpg', 
 u'full_name': u'Annie Lin', u'id': u'387829024'})
"""

class InstagramLib():
	def __init__(self):
		self.token = "387829024.a9a03de.832693a120bc4da183e39c982f030a8c"
		self.secret = "3fc9342ceedc412f99f646b6b9a5ae77"
	
	def get_client():
		api = InstagramAPI(access_token=self.token, client_secret=self.secret)
		return api

	def get_photos_location(latitude, longitude, count):
		api = self.get_client()
		loc = api.location_search(lng=longitude, lat=latitude, count=count)
		recent_media, next_ = api.location_recent_media(location_id = loc[0].id)
		return recent_media

   	def get_photos_user():
   		user_id = api.user_search('annielin143')[0].id
		recent_media, next_ = api.user_recent_media(user_id=user_id, count=10)
		return recent_media