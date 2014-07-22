# encoding: utf-8

import os
import sys
import requests
import time
import json

endpoint = 'http://api.sharedcount.com/'

def fetch(urls, prefix=None):
    name = 'shares'
    if prefix:
        name = prefix + '-' + name

    dest = 'data/{name}.json'.format(name=name)

    if os.path.exists(dest):
        print "{dest} already exists, skipping".format(dest=dest)
        return
    else:
        print "Fetching share counts for {length} articles".format(length=len(urls))

    shares = open(dest, 'w')
    for url in urls:
        try:
            response = requests.get(endpoint, params=params)
        except requests.exceptions.ConnectionError:
            sys.stdout.write('/')
            sys.stdout.flush()
            time.sleep(15)
            continue

        if response.status_code == 200:
            # we add the URL to the share data we just received, 
            # so we can link up article and share data later
            data = response.json()
            data['url'] = url
            serialization = json.dumps(data) + '\n'
            shares.write(serialization)
            sys.stdout.write('.')
            sys.stdout.flush()
        else:
            sys.stdout.write('~')
            sys.stdout.flush()
            time.sleep(5)

        time.sleep(0.25)

    sys.stdout.write('\n')