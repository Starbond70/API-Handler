from apis.nasa import get_apod
from apis.news import get_headlines
from apis.tech_trends import get_trending_languages
from apis.chaos_index import get_chaos_index
from core.sentiment import analyze_sentiment
from core.fortune_generator import generate_fortune
import os
from dotenv import load_dotenv

load_dotenv()

def run(city="Delhi"):
    apod = get_apod(os.getenv("NASA_API_KEY"))
    news = get_headlines(os.getenv("NEWS_API_KEY"))
    sentiment = analyze_sentiment(" ".join(news))
    trends = get_trending_languages()
    chaos = get_chaos_index()

    print(generate_fortune(apod, sentiment, chaos, trends))

if __name__ == "__main__":
    run()