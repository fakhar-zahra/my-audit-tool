# utils/heading_checker.py

import requests
from bs4 import BeautifulSoup

def check_headings(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')

        headings = {
            "h1": len(soup.find_all("h1")),
            "h2": len(soup.find_all("h2")),
            "h3": len(soup.find_all("h3")),
            "h4": len(soup.find_all("h4")),
            "h5": len(soup.find_all("h5")),
            "h6": len(soup.find_all("h6")),
        }
        return headings
    except Exception as e:
        return {"error": str(e)}
