import requests

def check_speed(url):
    try:
        response = requests.get(url, timeout=10)
        load_time = response.elapsed.total_seconds()
        return {
            "load_time_seconds": load_time
        }
    except Exception as e:
        return {
            "error": str(e)
        }
