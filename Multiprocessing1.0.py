from multiprocessing import *
import discord
from discord.ext import tasks
import praw
import tweepy
import random
import sys
import asyncio
import os
import time
import datetime

#I learned about multithreading and multiprocessing In one of my CompSci classes and wanted to visualize it a little better
#So during some downtime I had, I took some old code for a discord bot that crawls reddit and a twitter users account,
#and then it appends urls from r/memes and @beetlepimp's twitter account to an array so discord users could then
#command the bot to post a random meme/tweet. The origional code had to index r/memes first, then twitter (super inneficient)
#and had a total runtime of about 3 seconds but using multiprocessing and the same logic, I cut down the runtime by ~65%
#from 2.90 sec to 1.48. :) 


reddit = praw.Reddit(client_id = clientID, client_secret = clientSecret, user_agent = userAgent,check_for_async=False)

auth = tweepy.OAuthHandler(apiKey, apiSecretKey)
auth.set_access_token(accessToken, AccessTokenSecret)
api = tweepy.API(auth, wait_on_rate_limit = True)


def redditMemes():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print('start reddit scraping '+ str(current_time))

    for submission in reddit.subreddit('memes').hot(limit=1500):
        if submission.score > 700 and not submission.stickied:
            listOfMemes.append(submission.url + '\n**Up Votes:** ' + "*" + str(
                submission.score) + "*" + "\n**Subreddit:** " + "*r/memes*")
    runtime = time.process_time()
    print("Reddit done \nRuntime: " + str(runtime))

def beetTweets():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print('start twitter scraping ' + str(current_time))

    for tweet in tweepy.Cursor(api.user_timeline, id='BEETLEPIMP', result_type='popular').items(1400):
        tweetList.append(tweet.text)
    runtime = time.process_time()

    print("Twitter done \nRuntime: "+str(runtime))
    print("Total runtime: "+str(runtime))

if __name__ == '__main__':
    p1 = Process(target= redditMemes)
    p1.start()
    p2 = Process(target = beetTweets)
    p2.start()
    p1.join()
    p2.join()






