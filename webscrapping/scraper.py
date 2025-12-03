import requests
import requests

from bs4 import BeautifulSoup

# beautiful soup

url = "https://www.freelancer.com/"



try:
    response = requests.get(url)
except requests.exceptions.RequestException as e:
    print(f"Oops! Something went wrong. Maybe check your internet connection?: {e}")
except EOFError:
    print("Cannot scrape that website")
else:

    print(response.status_code)
    if response.status_code == 200:

        with open("freelancer.html", "w", encoding="utf-8") as f:
            soup = BeautifulSoup(response.text, 'html.parser')
            f.write(soup.prettify())

    else:
        print(f"That was unexpected, status code: {response.status_code}")
        print(response.text)