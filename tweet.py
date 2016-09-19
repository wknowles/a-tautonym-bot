#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, os

# import auth from heroku
CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']

# twitter auth
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

try:
    with open('tautonyms.txt', 'r+') as tweetfile:
        buff = tweetfile.readlines()

    for line in buff[:]:
        line = line.strip(r'\n') #Strips any empty line.
        if len(line)<=140 and len(line)>0:
            print ("Tweeting...", line)
            api.update_status(line)
            with open ('tautonyms.txt', 'w') as tweetfile:
                buff.remove(line) #Removes the tweeted line.
                tweetfile.writelines(buff)
            time.sleep(21600) #6 Hours
        else:
            with open ('tautonyms.txt', 'w') as tweetfile:
                buff.remove(line) #Removes the line that has more than 140 characters.
                tweetfile.writelines(buff)
            print ("Skipped line - Char length violation")
            continue
    print ("No more lines to tweet...") #When you see this... Well :) Go find some new tweets...

except tweepy.TweepError as e:
    print (e)
