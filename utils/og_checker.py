# utils/og_checker.py

import requests
from bs4 import BeautifulSoup

def check_open_graph(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')

        og_tags = {
            "og:title": None,
            "og:description": None,
            "og:image": None,
            "og:url": None
        }

        for tag in og_tags:
            og_tag = soup.find("meta", property=tag)
            if og_tag and og_tag.get("content"):
                og_tags[tag] = og_tag["content"]

        return og_tags
    except Exception as e:
        return {"error": str(e)}