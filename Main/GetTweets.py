import tweepy
import twitter_credentials
from TweetStatistics import TweetStatistics

class GetTweets:
    def __init__(self):
        self.auth = tweepy.OAuthHandler(consumer_key=twitter_credentials.CONSUMER_API_KEY, consumer_secret=twitter_credentials.CONSUMER_API_SECRET_KEY)
        self.auth.set_access_token(twitter_credentials.ACCESS_TOKEN_KEY, twitter_credentials.ACCESS_SECRET_KEY)
        self.api = tweepy.API(self.auth)
        self.user_input = ""
        self.tweet_count = 0


    def get_search_term(self):
        self.user_input = input("Enter a hashtag to search for - ")
        return self.user_input

    def get_number_of_tweets(self):
        self.tweet_count = int(input("How many tweets to sample - "))
        return self.tweet_count

    def run_search(self):
        tweets = tweepy.Cursor(self.api.search, q=self.get_search_term()).items(self.get_number_of_tweets())
        process_stats = TweetStatistics(tweets, self.user_input, self.tweet_count)
        process_stats.get_statistics()

