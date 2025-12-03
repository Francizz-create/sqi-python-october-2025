# import requests
# from bs4 import BeautifulSoup

# url = "https://www.flyfitness.ng/"
# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")

# quotes = soup.find_all("span", class_="text")
# authors = soup.find_all("small", class_="author")
    
# for q, a in zip(quotes, authors):
#     print(f"{q.text} — {a.text}")





import requests

from bs4 import BeautifulSoup

url = "https://www.flashscore.com/"

response = requests.get(url)

with open("https://www.flashscore.com/", "w") as f:
    soup = BeautifulSoup(response.text, 'html.parser')
    f.write(soup.prettify())



import requests
from bs4 import BeautifulSoup

url = "https://www.flashscore.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

with open("https://www.flashscore.com/", "w", encoding="utf-8") as f:
    f.write(soup.prettify())

print("HTML saved successfully to jumia-home.html")

# https://www.flyfitness.ng/