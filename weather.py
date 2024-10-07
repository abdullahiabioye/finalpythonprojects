import requests
from bs4 import BeautifulSoup

url = 'https://www.accuweather.com/en/ng/lagos/4607/current-weather/4607' 

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

titles = soup.find_all('h1')  

print("News Article Titles:")
for title in titles:
    print(title.get_text(strip=True))
