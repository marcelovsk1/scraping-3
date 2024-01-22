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

        event_date = event.find('div', class_=event_date)
        event_date = event_date.text.strip() if event_date else None

        event_location = event.find('div', class_=event_location)
        event_location = event_location.text.strip() if event_location else None

        image_elem = event.find('img', class_=image_url)
        image_url = image_elem['src'] if image_elem and 'src' in image_elem.attrs else None


        event_info = {
            'Event': event_name,
            'Date': event_date,
            'Location': event_location,
            'Image URL': image_url
        }

        event_list.append(event_info)

    driver.quit()

    return event_list

ticketmaster_url = 'https://www.ticketmaster.ca/discover/concerts/montreal'
ticketmaster_name = 'sc-fFeiMQ bCvzDL text text--dark text--primary sc-6jnhqk-0 kGOLzf event-tile__title'
ticketmaster_date = 'sc-fFeiMQ dBYlim text text--accent text--accent01 text-tm sc-17ev1tv-0 cnj20n-0 firocR iZsGLV event-tile__date-title'
ticketmaster_location = 'sc-fFeiMQ iIgzpz text text--dark text--secondary sc-1s3i3gy-0 hbRPym event-tile__sub-title'
ticketmaster_image = 'event-listing__thumbnail'

ticketmaster_events = scrape_events(ticketmaster_name, ticketmaster_date)


json_data = json.dumps(all_events, indent=2)

# Print or save the JSON data as needed
print(json_data)
