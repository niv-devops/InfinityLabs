# Approved by: Arin
import requests

TIMEOUT = 5

def availability_check(url):
    try:
        response = requests.get(url, verify=False, timeout=5)
        if 200 <= response.status_code < 300:
            print(f"The website in {url} is reachable.")
            return True
        else:
            print(f"The website in {url} is unreachable, status code {response.status_code}.")
            return False
     
    except requests.ConnectionError as e:
        print(f"The website in {url} is unreachable, Error: {str(e)}")
        return False

    except requests.exceptions.Timeout as e:
        print(f"Website in {url} is uneachable, connection timed out after {TIMEOUT} seconds.")
        return False
    
    except requests.exceptions.RequestException as e:
        print(f"The website in {url} is unreachable, Error: {str(e)}")
        return False


if __name__ == "__main__":
    availability_check("https://www.google.com")
    availability_check("https://10.1.0.8:9090")
    availability_check("https://goofy.servebeer.com")