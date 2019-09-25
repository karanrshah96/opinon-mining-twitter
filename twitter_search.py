def tsearch(q1, q2):
    import tweepy
    import csv
    ckey = "61cK90bUwNg9Bh7dhT1KQuGFB"
    csecret = "djSmsVDJb2iMZ138t6DXK6K0u7mpvqRLbj678pzbTgeGDgNdX1"
    atoken = "2153329357-yXtzeiEOIpuxczMkof7UUg8SluYcvDxx9uXnYLK"
    asecret = "GiVlShJlavgdNnnu6ntjXvRl6LCTvywoJWn6mR7O2lnN7"
    OAUTH_KEYS = {'consumer_key': ckey, 'consumer_secret': csecret,
                  'access_token_key': atoken, 'access_token_secret': asecret}
    auth = tweepy.OAuthHandler(OAUTH_KEYS['consumer_key'], OAUTH_KEYS['consumer_secret'])
    api = tweepy.API(auth)

    Tweet1 = tweepy.Cursor(api.search, q=q1).items(100)
    Tweet2 = tweepy.Cursor(api.search, q=q2).items(100)

    list1 = []
    list2 = []
    for tweet in Tweet1:
        if(tweet.lang == "en"):
            list1.append(tweet.text.encode('utf-8'))

    for tweet in Tweet2:
        if(tweet.lang == "en"):
            list2.append(tweet.text.encode('utf-8'))

    with open("q1.csv", 'wb') as g:
        writer = csv.writer(g)
        writer.writerow(['SentimentText'])
        for item in list1:
            writer.writerow([item])

    with open("q2.csv", 'wb') as g:
        writer = csv.writer(g)
        writer.writerow(['SentimentText'])
        for item in list2:
            writer.writerow([item])
    print '---------'
