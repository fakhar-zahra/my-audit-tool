from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def capture_screenshot(url, output_path="screenshot.png"):
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--window-size=1920,1080")

        driver = webdriver.Chrome(options=chrome_options)

        driver.get(url)

        page_height = driver.execute_script("return document.body.scrollHeight")
        driver.set_window_size(1920, page_height)

        driver.save_screenshot(output_path)
        driver.quit()

        return output_path
    except Exception as e:
        print(f"Error capturing screenshot: {e}")
        return None
