import birdfeeder
import ujson
import sys

tweets = birdfeeder.list_timeline(owner_screen_name="cspan", slug="members-of-congress")

for tweet in tweets:
  sys.stdout.write(ujson.dumps(tweet) + "\n")
