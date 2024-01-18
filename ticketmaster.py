from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

url = 'https://www.ticketmaster.ca/search?sort=date&startDate=2024-01-18&endDate=2024-02-29'

options = Options()
options.headless = True

driver = webdriver.Chrome(options=options)
driver.get(url)
driver.implicitly_wait(10)

page_content = driver.page_source
webpage = BeautifulSoup(page_content, 'html.parser')

events = webpage.find_all('div', class_='sc-fyofxi-0 MDVIb')

for event in events:
    event_name = event.find('span', class_='sc-fyofxi-5 gJmuwa').text
    event_date_month = event.find('div', class_='sc-1evs0j0-1 gwWuEQ').text.strip()

    print(f"{event_name}")
    print(f"{event_date_month}")
    # print(event.text)

driver.quit()
