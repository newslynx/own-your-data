import os
from datetime import date
from pprint import pprint
import json
import googleanalytics as ga

client = dict(
    client_id='your_app_id', 
    client_secret='your_app_secret'
)

def authenticate():
    if os.path.exists('tokens.json'):
        tokens = json.load(open('tokens.json'))
    else:
        tokens = ga.oauth.ask(**client)
        json.dump(tokens, open('tokens.json', 'w'), indent=4)

    return ga.oauth.authenticate(**tokens)

def first(accounts):
    print accounts
    account = accounts[0]
    print account.webproperties
    prop = account.webproperties[0]
    profile = prop.profiles[0]
    print profile
    return profile

def query(profile):
    query = profile.query('pageviews').days('2014-06-01', days=3)
    report = query.execute()

    print report['pageviews']


if __name__ == '__main__':
    accounts = authenticate()
    profile = first(accounts)
    query(profile)