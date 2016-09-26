#!/usr/bin/env python
# -*- coding: utf-8 -*-

# taxonomy taken from list of Classical Latin proper names: https://github.com/cltk/latin_proper_names_cltk

import tweepy, random

# Not needed for heroku - twitter auth is done through config vars added to heroku
#
# # import twitter creds from secrets.py
# from secrets import *
#
# # twitter auth
# auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
# auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
# api = tweepy.API(auth)

# bot setup
date = random.randrange(1735, 2016)
genus = random.choice(open('corpus/proper_names.txt').readlines()).rstrip('\n').lower()
binomial = genus.title() + " " + genus
authority = random.choice(open('corpus/authority.txt').readlines()).rstrip('\n')
#TODO: perhaps have random parenthesis around authority and date - the parentheses indicate that the species is now considered to belong in a different genus
tweet = "%s (%s, %i)" % (binomial, authority, date)

# check length and then tweet
if len(tweet)<=140 and len(tweet)>0:
    print "Tweeting ====> ", tweet
    #api.update_status(tweet)
else:
    print "Skipped tweet - too long!"
