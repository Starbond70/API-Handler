import requests

def get_headlines(api_key):
    url = f"https://newsapi.org/v2/top-headlines?language=en&pageSize=5&apiKey={api_key}"
    data = requests.get(url).json()
    return [article["title"] for article in data["articles"]]