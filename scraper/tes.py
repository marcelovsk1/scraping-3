import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import time

def scrape_events(url, event, event_name, event_date, event_location, image_url):
    options = Options()
    options.headless = True

    driver = webdriver.Chrome(options=options)
    driver.get(url)
    driver.implicitly_wait(10)

    click_count = 0
    max_clicks = 3

    def click_load_more():
        nonlocal click_count
        while click_count < max_clicks:
            try:
                load_more_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Load More')]")
                ActionChains(driver).move_to_element(load_more_button).perform()
                load_more_button.click()
                time.sleep(3)
                click_count += 1
            except Exception as e:
                print(f"Unable to find or click the 'Load More' button: {e}")
                break

    click_load_more()

    page_content = driver.page_source
    webpage = BeautifulSoup(page_content, 'html.parser')

    events = webpage.find_all('div', class_=event_class)

    event_list = []

    for event in events:
        event_name = event.find('div', class_=event_name)
        event_name = event_date.text if event_name else None
