from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

url = 'https://www.facebook.com/events/explore/montreal-quebec/102184499823699/'

options = Options()
options.headless = True

driver = webdriver.Chrome(options=options)
driver.get(url)
driver.implicitly_wait(10)

page_content = driver.page_source
webpage = BeautifulSoup(page_content, 'html.parser')
events = webpage.find_all('div', class_='x78zum5 x1n2onr6 xh8yej3')

for event in events:
    event_image = event.find('img', class_='x1rg5ohu x5yr21d xl1xv1r xh8yej3')

    image_url = event_image['src'] if event_image and 'src' in event_image.attrs else None

    print(event.text)
    print(f"Image URL: {image_url}")

driver.quit()
