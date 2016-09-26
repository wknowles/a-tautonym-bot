#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, os, random
from datetime import date


# import auth from heroku
CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']

# twitter auth
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# bot setup
date = random.randrange(1735, date.today().year)
genus = random.choice(open('corpus/proper_names.txt').readlines()).rstrip('\n').lower()
binomial = genus.title() + " " + genus
authority = random.choice(open('corpus/authority.txt').readlines()).rstrip('\n')
tweet = "%s (%s, %i)" % (binomial, authority, date)

# check length and then tweet
if len(tweet)<=140 and len(tweet)>0:
    api.update_status(tweet)
else:
    print "Skipped tweet - too long!"
