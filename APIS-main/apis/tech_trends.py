import requests
from bs4 import BeautifulSoup

def get_trending_languages():
    url = "https://github.com/trending"
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    repos = soup.find_all("article", class_="Box-row")
    languages = [repo.find('span', itemprop='programmingLanguage') for repo in repos]
    return [lang.text for lang in languages if lang][:5]