from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentiment_mod as s

#consumer key, consumer secret, access token, access secret.
ckey="XziNR8rIJXlcevuWDJ5u9yH6J"
csecret="24lEPKsHENsE9B0zszY7nSEg3837sUqP66mx6S1qBK3huzXLIN"
atoken="939419825360683008-BW8sOY8xZFnuOvUnK0qJHcgPvAWIS8I"
asecret="5hxVYBZwekNpaf0YSkCxVVD4MC6j0473L0QiI0FoubcE2"



class listener(StreamListener):

    def on_data(self, data):

        all_data = json.loads(data)
        tweet = all_data["text"]
        sentiment_value, confidence = s.sentiment(tweet)
        print(tweet, sentiment_value, confidence)
        if confidence*100 >= 80:
            output = open("twitter-out.txt","a")
            output.write(sentiment_value)
            output.write('\n')
            output.close()

            return True

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["happy"])
