import requests
from bs4 import BeautifulSoup

# Step 1: Fetch the page
url = "http://quotes.toscrape.com"
response = requests.get(url)
html = response.text

# Step 2: Parse the HTML
soup = BeautifulSoup(html, "html.parser")

# Step 3: Extract quotes and authors
quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")

# Step 4: Display results
for q, a in zip(quotes, authors):
    print(f"{q.text} — {a.text}")