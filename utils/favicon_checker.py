# utils/favicon_checker.py

import requests
from bs4 import BeautifulSoup

def check_favicon(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        icon_link = soup.find("link", rel=lambda x: x and 'icon' in x.lower())

        if icon_link and icon_link.get('href'):
            return {"favicon_found": True, "favicon_url": icon_link.get('href')}
        else:
            return {"favicon_found": False, "favicon_url": None}
    except Exception as e:
        return {"error": str(e)}
