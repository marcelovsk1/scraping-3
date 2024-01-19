from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

url = 'https://www.ticketmaster.ca/discover/concerts/montreal'

options = Options()
options.headless = True

driver = webdriver.Chrome(options=options)
driver.get(url)
driver.implicitly_wait(10)

page_content = driver.page_source
webpage = BeautifulSoup(page_content, 'html.parser')

events = webpage.find_all('div', class_='Flex-sc-145abwg-0 bWTqsV accordion__item event-listing__item')

for event in events:
    event_name = event.find('div', class_='sc-fFeiMQ bCvzDL text text--dark text--primary sc-6jnhqk-0 kGOLzf event-tile__title').text
    event_date = event.find('div', class_='sc-fFeiMQ dBYlim text text--accent text--accent01 text-tm sc-17ev1tv-0 cnj20n-0 firocR iZsGLV event-tile__date-title').text.strip()
#     event_day = event.find('div', class_='sc-1evs0j0-2 ftHsmv').text.strip()
    event_location = event.find('div', class_='sc-fFeiMQ iIgzpz text text--dark text--secondary sc-1s3i3gy-0 hbRPym event-tile__sub-title').text.strip()

    print(f"Event: {event_name}")
    print(f"Date: {event_date}")
#     print(f"{event_day}")
    print(f"Location: {event_location}")

driver.quit()
