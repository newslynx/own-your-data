import birdfeeder 
import ujson
import sys

"""
## Getting API credentials for Twitter.

1. Go to http://dev.twitter.com/.

2. Create an APP.

3. Find your:
  - api_key
  - api_secret
  - access_token
  - access_secret

4. Store these as environmental variables:

  - TWT_API_KEY
  - TWT_API_SECRET
  - TWT_ACCESS_TOKEN
  - TWT_ACCESS_SECRET


## WORKING WITH THE TWITTER STREAMING API (via birdfeeder)

birdfeeder's twitter streaming API client works as follows:

You define three functions.

1. How to parse the data.

2. How to store the data.

3. What to do with errors.

By default, it uses an opinionated parser for (1) that gets most everything you want 
while doing some other nice things like unshortening and standardizing URLs, and ignores all errors for (3).

The easiest way to store this data is to just write it to a line-separated json file, though its
not too hard to write to a SQL database, redis, elastic search, s3, etc, etc, etc.

## FILTERING THE TWITTER STREAMING API 

The public streaming API works as follows:

- If you track nothing, you can get a 1% sample of the firehose.
- However, if you search for a specific term or set of terms which doesn't represent more than 
  1 % of the firehose, you will get ALL of the matching tweets.

## TRACKING URL's / DOMAINS ON THE TWITTER STREAMING API

- Tracking domains is tricky on twitter, but super useful.  

- Imagine a simple way to store every mention of your news site's domain! 
  You could just setup a column in TweetDeck, but this way you can analyze 
  the data for yourself.

- To track a domain on Twitter, you need to create a search term that "looks like" the domain.
  (see here for reference: https://dev.twitter.com/docs/streaming-apis/parameters)

- For instance, if you want to find all mentions of www.nytimes.com, you would search for "www nytimes com"

- Alternatively, if you wanted to find short url mentions, you could search for "nyti ms"

- Finally, if you use birdfeeder's default parser, it will unshorten all URLs for you.

"""
terms = ["nytimes com", "nyti ms"]

def _print(data):
  sys.stdout.write(ujson.dumps(data) + "\n")

s = birdfeeder.Stream(store=_print)
s.statuses.filter(track=terms)


