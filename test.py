#!/usr/bin/env python
# encoding: utf-8
import sys

import tweepy  # https://github.com/tweepy/tweepy

# Twitter API credentials
consumer_key = "x1ZcTUl6KV6lxKkgcb51j91lI"
consumer_secret = "VFXPt4Gk6EwX4KbomR1HIAd9ObHjiWi5yMk5zyHbmjDPX07nMA"
access_key = "865138923282018304-VUvrEYMlCQRtRNX6OJYIFmZDTzRB5Yw"
access_secret = "QFYPrNqppR9gs2oWsVabv3TJpQPY6K5RcvyT2u4jih9Cg"

def get_all_tweets(screen_name):
    # Twitter only allows access to a users most recent 3240 tweets with this method

    # authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    # initialize a list to hold all the tweepy Tweets
    alltweets = []

    # make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name=screen_name, count=200)

    # save most recent tweets
    alltweets.extend(new_tweets)

    # save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    #q = '#MentionSomeoneImportantForYou'

    # keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        print "getting tweets before %s" % (oldest)

        # all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name=screen_name, count=200, max_id=oldest)

        # save most recent tweets

        alltweets.extend(new_tweets)



        # update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        print "...%s tweets downloaded so far" % (len(alltweets))

    # transform the tweepy tweets into a 2D array that will populate the csv
        outtweets = [tweet.text for tweet in alltweets]
        #print outtweets
        f=open('testfile.txt','w')
        f.write(str(outtweets))
        f.close()

    pass
# to encode the data
reload(sys)
sys.setdefaultencoding('utf-8')

#word_tokenize accepts a string as an input, not a file.
if __name__ == '__main__':
	#pass in the username of the account you want to download
    get_all_tweets("tusharkute")



