# encoding: utf-8

import pandas as pd
from datetime import date, timedelta
import json
import fetchers
import utils

"""
Let's go from our article JSON to a nice tabular data structure.
"""

def munge(from_date, to_date):
    articles = fetchers.load('articles', from_date, to_date)
    articles = utils.index_by(articles, 'webUrl')

    for url, article in articles.items():
        # put all tags in a single field, separated by commas 
        # and get rid of all metadata we don't need
        tags = [tag['id'] for tag in article['tags'] if tag['type'] == 'keyword']
        article['tags'] = ", ".join(tags)
        # flatten the article datastructure that was 
        # returned by the Content API
        articles[url] = utils.flatten(article)

    # For our purposes, it's nicer to have fields like "title" etc. 
    # be columns rather than rows, so we make a data frame and then 
    # transpose it, essentially rotating it by 90 degrees.
    articles = pd.DataFrame(articles).transpose()

    """
    Okay, now it's time to get our share counts into shape.
    It's mostly the same process we used for articles: load, 
    flatten, index, add to a DataFrame.
    """

    shares = fetchers.load('shares', from_date, to_date)
    shares = [utils.flatten(d) for d in shares]
    shares = utils.index_by(shares, 'url')
    shares = pd.DataFrame(shares).transpose()

    """
    Let's pull it all together.
    """

    articles = articles.join(shares)

    # this is just aesthetics, but we're going to normalize all 
    # column names so they're all lowercase and use dashes
    # instead of spaces
    articles = utils.normalize_columns(articles)

    return articles