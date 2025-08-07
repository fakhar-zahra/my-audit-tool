import requests
from bs4 import BeautifulSoup

def check_seo_tags(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        title = soup.title.string if soup.title else "No title"
        meta_description = "No description"
        description_tag = soup.find("meta", attrs={"name": "description"})
        if description_tag and description_tag.get("content"):
            meta_description = description_tag["content"]

        return {
            "title": title,
            "description": meta_description
        }
    except Exception as e:
        return {
            "error": str(e)
        }
