from textblob import TextBlob
import pandas as pd
import numpy as np
import math

class TweetStatistics:

    def __init__(self, tweets, user_input, tweet_count):
        self.tweets = tweets
        self.positive = 0
        self.neutral = 0
        self.negative = 0
        self.subjectivity = 0
        self.user_input = user_input
        self.tweet_count = tweet_count

    def get_statistics(self):
        for tweet in self.tweets:
            blob = TextBlob(tweet.text)
            self.subjectivity += blob.sentiment.subjectivity
            # print(tweet.created_at)
            self.rate_polarity(blob.sentiment.polarity)

        self.print_output()

    def rate_polarity(self, polarity):
        if polarity > 0.0 and polarity <= 1.0:
            self.positive += 1
        elif polarity == 0.0:
            self.neutral += 1
        elif polarity < 0.0:
            self.negative += 1

    def calculate_subjectivity(self):
        return round((self.subjectivity / self.tweet_count), 2)


    def print_output(self):
        print("\nTweet analysis for the #{}\n".format(self.user_input))
        data_frame = pd.DataFrame({
            'Positive': self.positive,
            'Negative': self.negative,
            'Neutral': self.neutral,
            'Subjectivity': self.calculate_subjectivity(),
            'Sample Size': self.tweet_count
        }, index = [self.user_input])

        print(data_frame)
