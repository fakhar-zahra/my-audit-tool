# utils/links_checker.py

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def check_links(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        links = soup.find_all('a', href=True)

        total_links = len(links)
        internal_links = 0
        external_links = 0

        for link in links:
            href = link['href']
            full_url = urljoin(url, href)

            if url in full_url:
                internal_links += 1
            else:
                external_links += 1

        return {
            "total_links": total_links,
            "internal_links": internal_links,
            "external_links": external_links
        }
    except Exception as e:
        return {"error": str(e)}
