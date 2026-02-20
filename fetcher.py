import requests
from bs4 import BeautifulSoup
from config import NEWS_API_KEY


def fetch_from_newsapi(source=None):
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "apiKey": NEWS_API_KEY,
        "country": "us",
        "pageSize": 20
    }

    if source:
        params["sources"] = source

    response = requests.get(url, params=params)
    data = response.json()

    articles = []
    for article in data.get("articles", []):
        articles.append({
            "title": article["title"],
            "source": article["source"]["name"],
            "date": article["publishedAt"][:10],
            "url": article["url"]
        })

    return articles


def fetch_from_bbc():
    url = "https://www.bbc.com/news"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    articles = []
    headlines = soup.find_all("h3")

    for h in headlines[:15]:
        articles.append({
            "title": h.text.strip(),
            "source": "BBC",
            "date": "",
            "url": url
        })

    return articles