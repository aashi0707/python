#!/usr/bin/python2

import  tweepy
import  sys
topic=sys.argv[1]
consumer_key='6kYlncj9BOkSJtdy17aB2HetN'
consumer_sec='nrYuwEPQIjmFp4TTjZcjs5S0dtU5QypJooCrc6MysfqWuePiuN'
#  by using above keys  we are going to check auth handler 
auth=tweepy.OAuthHandler(consumer_key,consumer_sec)
#  here auth is token by consuker key and sec 
access_key='1070575453474357249-xcVpIolxL9RUgFw7cGS9Vlv4wafxya'
secret_key='iGT71SjSihvCqg2TH1oh9Xw3QXh2mCA2pnzYToeR9YeiC'
#  connecting  data server  with  access and secret key  by using above token
print(dir(auth))
auth.set_access_token(access_key,secret_key)
#  connecting to twitter api with  token that is stored in auth
connected=tweepy.API(auth)

#  searching topics 
tweet=connected.search(topic,count=10)

print  tweet
#  converting into text
for  j  in  tweet:
	print  j.text

'''
#  connecting with twitter handler 
user1=connected.get_user('Ashut0shh')
print(dir(user1))
print "okeyyyyyyyyyyyyyyyyyy",user1.followers_count
'''
