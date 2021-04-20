from datetime import date
import datetime
from db.handle_tweets_module.twintScripts import saveTweetsByHashtag, saveUserByName


def saveTweetsByHashtagList(hashtagList, startDate=datetime.datetime(2020, 10, 1), endDate=date.today(), username=None):
    for hashtag in hashtagList:
        print('\033[96m' + "saving tweets for hashtag: " + hashtag + '\033[0m')
        saveTweetsByHashtag(hashtag,  startDate, endDate, username)


def saveUsers(usersList):
    for userName in usersList:
        try:
            saveUserByName(userName)
        except Exception as e:
            print(e)


def saveTweetsByHashtagListForAllUsers(hashtagList, userList, startDate=datetime.datetime(2020, 10, 1), endDate=date.today()):
    for hashtag in hashtagList:
        for user in userList:
            print('\033[96m' + "saving tweets for hashtag: " + hashtag + " for user: " + user + '\033[0m')
            saveTweetsByHashtag(hashtag,  startDate, endDate, user)
