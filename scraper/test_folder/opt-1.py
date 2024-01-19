import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import time

def click_load_more(driver, max_clicks=5):
    click_count = 0
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

def scrape_eventbrite_events(driver):
    event_list = []

    events = driver.find_elements(By.CLASS_NAME, 'Stack_root__1ksk7')

    for event in events:
        event_name = event.find_element(By.TAG_NAME, 'h2').text if event.find_element(By.TAG_NAME, 'h2') else None
        event_date = event.find_element(By.TAG_NAME, 'p').text.strip() if event.find_element(By.TAG_NAME, 'p') else None
        event_location_element = event.find_element(By.XPATH, "//p[contains(@class, 'Typography_root__487rx')]")
        event_location = event_location_element.text.strip() if event_location_element else None
        event_image = event.find_element(By.CLASS_NAME, 'event-card-link')
        image_url = event_image.get_attribute('href') if event_image else None

        event_info = {
            'Event': event_name,
            'Date': event_date,
            'Location': event_location,
            'Image URL': image_url
        }

        event_list.append(event_info)

    return event_list

def scrape_ticketmaster_events(driver):
    event_list = []

    events = driver.find_elements(By.CLASS_NAME, 'Flex-sc-145abwg-0')

    for event in events:
        try:
            event_name = event.find_element(By.CLASS_NAME, 'sc-fFeiMQ').text
        except NoSuchElementException:
            event_name = None

        try:
            event_date = event.find_element(By.CLASS_NAME, 'sc-fFeiMQ.dBYlim').text.strip()
        except NoSuchElementException:
            event_date = None

        try:
            event_location = event.find_element(By.CLASS_NAME, 'sc-fFeiMQ.iIgzpz').text.strip()
        except NoSuchElementException:
            event_location = None

        try:
            event_image = event.find_element(By.CLASS_NAME, 'event-listing__thumbnail')
            image_url = event_image.get_attribute('src')
        except NoSuchElementException:
            image_url = None

        event_info = {
            'Event': event_name,
            'Date': event_date,
            'Location': event_location,
            'Image URL': image_url
        }

        event_list.append(event_info)

    return event_list


url_eventbrite = 'https://www.eventbrite.com/d/canada--montreal/events/'
url_ticketmaster = 'https://www.ticketmaster.ca/discover/concerts/montreal'

options = Options()
options.headless = True

driver = webdriver.Chrome(options=options)

# Scrape data from Eventbrite
driver.get(url_eventbrite)
driver.implicitly_wait(10)
eventbrite_events = scrape_eventbrite_events(driver)

# Scrape data from Ticketmaster
driver.get(url_ticketmaster)
driver.implicitly_wait(10)
click_load_more(driver)
ticketmaster_events = scrape_ticketmaster_events(driver)

# Combine the event lists
all_events = eventbrite_events + ticketmaster_events

# Convert the list of dictionaries to a JSON-formatted string
json_data = json.dumps(all_events, indent=2)

# Print or save the JSON data as needed
print(json_data)

driver.quit()
