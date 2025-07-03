import requests

def get_apod(api_key):
    url = "https://api.nasa.gov/planetary/apod"
    params = {"api_key": api_key}
    response = requests.get(url, params=params)
    data = response.json()
    return {
        "title": data.get("title"),
        "description": data.get("explanation")
    }