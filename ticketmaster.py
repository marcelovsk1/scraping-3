from bs4 import BeautifulSoup
import requests

url = 'https://www.ticketmaster.ca/search?q='
page = requests.get(url)

webpage = BeautifulSoup(page.content, 'html.parser')

events = webpage.find_all('li', attrs={'class': 'sc-fyofxi-0 MDVIb'})

for event in events:
    event_name = event.find('span', attrs={'class': 'sc-fyofxi-5 gJmuwa'}).text

    print(f"{event_name}")
