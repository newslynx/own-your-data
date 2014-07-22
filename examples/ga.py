import os
from datetime import date
from pprint import pprint
import json
import googleanalytics as ga

client = dict(
    client_id='your_app_id', 
    client_secret='your_app_secret'
)

def authenticate_fs():
    if os.path.exists('tokens.json'):
        tokens = json.load(open('tokens.json'))
    else:
        tokens = ga.oauth.ask(**client)
        json.dump(tokens, open('tokens.json', 'w'), indent=4)

    return ga.oauth.authenticate(**tokens)

def authenticate_keyring():
    """ a nicer way to authenticate for projects that 
    only run on your local machine """
    return ga.utils.keyring.ask_and_authenticate('my-app', **client)    

def first(accounts):
    print accounts
    account = accounts[0]
    print account.webproperties
    prop = account.webproperties[0]
    profile = prop.profiles[0]
    print profile
    return profile

def query(profile):
    """
    Here's the basic list of query methods:

        query
            .sort
            .filter
            .range
            .hours
            .days
            .weeks
            .months
            .years
            .limit
            .segment
    """

    query = profile.query('pageviews').days('2014-06-01', months=1)
    report = query.execute()
    print report['pageviews']


if __name__ == '__main__':
    accounts = authenticate_keyring()
    profile = first(accounts)
    query(profile)
