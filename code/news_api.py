import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("NEWS_API_KEY")

def get_articles():
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "country": "us",
        "pageSize": 20,
        "apiKey": API_KEY
    }
    response = requests.get(url, params=params)
    data = response.json()

    return data.get("articles", [])
 

"This file connects to the NewsAPI service using an API key "
"stored securely in an environment variable"