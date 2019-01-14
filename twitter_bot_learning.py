import tweepy

print("This is a twitter test application")


Consumer_key='uleC7WN2wsuOKEdAFRhxPQNos'
Consumer_s_key='UzMpX9CcyzXCdgAdUjNRRChyaMKksZ5J6m8TyWNPxOdnUjdZAM'
Access_key='1084466746302648320-hOdvBLVwfbmX3R3vkNU8gbptrg6XY2'
Access_s_key='exysFsmi54Cqt5tKWnFVugSHtiN5fO29QYlRUDKI7B0qW'

auth=tweepy.OAuthHandler(Consumer_key, Consumer_s_key)
auth.set_access_token(Access_key,Access_s_key)

api=tweepy.API(auth)

mentions = api.mentions_timeline()





print(type(mentions))


for mention in mentions:
	print(mention.text)

