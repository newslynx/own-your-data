import birdfeeder 
import ujson
import sys

tweets = birdfeeder.user_timeline(screen_name = 'newslynx')

for tweet in tweets:
  sys.stdout.write(ujson.dumps(tweet) + "\n")