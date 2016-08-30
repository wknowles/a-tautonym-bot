#!/usr/bin/env python
# -*- coding: utf-8 -*-

# a super quick bot with thanks to http://www.dototot.com/how-to-write-a-twitter-bot-with-python-and-tweepy/

import tweepy, time, sys
#from secrets import * #import twitter creds

CONSUMER_KEY = "rnySqpVrGtGw8BmsEAMEORdsQ"
CONSUMER_SECRET = "bpH2V6VM6L8FymSyuaIoYHJfW0jOIRQwJAmh4j5YA9VwNk0xZw"
ACCESS_TOKEN = "767719595079786496-KA0uSGDFznMLTwyKKg4LTYqz5Wb8vHq"
ACCESS_TOKEN_SECRET = "vZY98SzA8y4lrBZ5zcXMdIWhd6SGM9jWQifkCX1W3D1c8"

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
