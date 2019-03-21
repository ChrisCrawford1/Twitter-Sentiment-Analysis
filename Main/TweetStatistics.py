from textblob import TextBlob

class TweetStatistics:

    def __init__(self, tweets):
        self.tweets = tweets
        self.positive = 0
        self.neutral = 0
        self.negative = 0

    def get_statistics(self):
        for tweet in self.tweets:
            blob = TextBlob(tweet.text)
            self.rate_polarity(blob.sentiment.polarity)

        return {"positive": self.positive, "neutral": self.neutral, "negative": self.negative}

    def rate_polarity(self, polarity):
        if polarity > 0.0 and polarity <= 1.0:
            self.positive += 1
        elif polarity == 0.0:
            self.neutral += 1
        elif polarity < 0.0:
            self.negative += 1