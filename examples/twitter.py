import os
import tweepy

api_key = os.environ['TWITTER_API_KEY']
api_secret = os.environ['TWITTER_API_SECRET']
token_key = os.environ['TWITTER_ACCESS_TOKEN']
token_secret = os.environ['TWITTER_ACCESS_TOKEN_SECRET']
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(token_key, token_secret)

api = tweepy.API(auth)

if __name__ == '__main__':
    # which of your tweets got retweeted?
    for status in api.retweets_of_me():
        print status.user.screen_name, status.retweet_count, status.text

    # The Search API can be a surprising source of insight, 
    # don't discount it!
    for status in api.search('ProPublica'):
        print status.text