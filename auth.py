import tweepy

#Twitter API Auth

consumer_key ="R7jRA4ThpH9n0OHHgeSEK8g4I"
consumer_secret="llrh1DdgFzC7GZe6OojXFQDJakC3OAChtlzgmT8PwhhhwGajeA"

access_token ="1316120547940593671-QiDI4IRcVJ8SnQZgxg3V93qOCrdBGv"
access_token_secret="iKVwhHpYS4xLSDxu8AYwPDNRqHIqOJoXQEAjWSG5nKawI"

# authentication object 

auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api= tweepy.API(auth)

