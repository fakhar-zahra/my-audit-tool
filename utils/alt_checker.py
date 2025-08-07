import requests
from bs4 import BeautifulSoup

def check_alt_text(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        images = soup.find_all("img")
        missing_alt = []

        for img in images:
            if not img.get("alt"):
                missing_alt.append(str(img))

        return {
            "total_images": len(images),
            "missing_alt_count": len(missing_alt),
            "missing_alt_images": missing_alt
        }
    except Exception as e:
        return {
            "error": str(e)
        }

