import tweepy
import time

api_key = "VNUO8LhJP0YqPyASd4dyKxXXU"
api_secret = "LGI1vx3PyktsnGqETe4tDFTFMS6R98broeLAb846TW21yerYkV"
bearer_token = r"AAAAAAAAAAAAAAAAAAAAAGZynwEAAAAAq4gY7nsUCbcBphYGtx%2BiqXJLnX4%3DftNVI7se1asDUwKaEkPQc96InlgQYxARbFTmQ1g3p5xwltu1bq"
access_token = "1208516892585058304-kyNGdpUVYETKoZBbMiF3xpIJrbPROk"
access_token_secret = "4JgaXzi5BlfWkh0z22IKNDKvjfcSwORwfCWomXPrmUmPa"

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

class MyStream(tweepy.StreamListener):
    def on_status(self, status):
        print(status.text)

        try:
            api.retweet(status.id)

        except tweepy.TweepError as error:
            print(error)

        time.sleep(1)

stream = MyStream()
stream_listener = tweepy.Stream(auth=api.auth, listener=stream)
rule = tweepy.stream.Rule("(Virat Kohli)(-is:retweet -is:reply)")
stream_listener.add_rule(rule)
stream_listener.filter()
