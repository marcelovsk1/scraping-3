from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

url = 'https://ra.co/events/ca/montreal'

options = Options()
options.headless = True

driver = webdriver.Chrome(options=options)
driver.get(url)
driver.implicitly_wait(10)

page_content = driver.page_source
webpage = BeautifulSoup(page_content, 'html.parser')

events = webpage.find_all('div', class_='Box-omzyfs-0 guLsXx')

for event in events:
    print(event)

driver.quit()
