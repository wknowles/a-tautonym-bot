#!/usr/bin/env python
# -*- coding: utf-8 -*-

# a super quick bot with thanks to http://www.dototot.com/how-to-write-a-twitter-bot-with-python-and-tweepy/

import tweepy, time, sys
from secrets import * #import twitter creds

argfile = str(sys.argv[1])

# twitter auth
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


filename=open(argfile,'r')
f=filename.readlines()
filename.close()

for line in f:
    api.update_status(line)
    time.sleep(3600)#Tweet every hour
