import datetime
from datetime import date
import twint


def saveTweetsByHashtag(hashtag, startDate=datetime.datetime(2020, 10, 1), endDate=date.today(), username=None):
    # Configure
    c = twint.Config()
    c.Username = username
    c.Since = str(startDate)
    c.Until = str(endDate)
    c.Filter_retweets = True
    c.Search = hashtag
    c.Count = True
    c.Database = "../tweets_20.05.db"
    c.Hide_output = True
    # Run
    twint.run.Search(c)
    # store in RAM:
    # tweets = []
    # c.Store_object_tweets_list = tweets
    # c.Store_object = True
    # return tweets


def saveUserByName(username):
    c = twint.Config()
    c.Username = username
    c.User_full = True
    c.Database = "../tweets_20.05.db"
    c.Hide_output = True
    twint.run.Lookup(c)
    # store in RAM:
    # c.Store_object = True
    # return twint.output.users_list[0]
