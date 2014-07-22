import json
import pandas as pd
from datetime import date
import nsa

def load_facebook():
    return pd.from_csv('facebook/normalized-facebook-insights-post-level-data.csv')

def load_nsa():
    FROM_DATE = date(2013,6,3)
    TO_DATE = date(2013,6,30)
    articles = nsa.munge(FROM_DATE, TO_DATE)
    return articles

def load_pollster():
    return json.load(open('pollster/pollster.json'))

def load(name):
    fn = "_".join(['load', name])
    return globals()[fn]()