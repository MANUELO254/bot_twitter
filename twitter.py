import tweepy

api_key =""
api_secret = ""
bearer_token = r""
access_token = ""
access_token_secret = ""

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)


#client.create_tweet(text = "I just made a twitter bot. lucky you")

#client.like("1664639662562988033")

client.retweet("1664639662562988033")

client.create_tweet(in_reply_to_tweet_id="1664639662562988033", text="what are the 3 fundamental rules of robots then?")

for tweet in api.home_timeline():
    print(tweet.text)
 