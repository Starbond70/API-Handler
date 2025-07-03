from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
nltk.download("vader_lexicon")

sia = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    score = sia.polarity_scores(text)
    if score['compound'] > 0.2:
        return "positive"
    elif score['compound'] < -0.2:
        return "negative"
    return "neutral"