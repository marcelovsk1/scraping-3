import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import time

def scrape_events(url, event_class, event_name_class, event_date_class, event_location_class, image_url_class):
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
        event_name_elem = event.find('div', class_=event_name_class)
        event_name = event_name_elem.text if event_name_elem else None

        event_date_elem = event.find('div', class_=event_date_class)
        event_date = event_date_elem.text.strip() if event_date_elem else None

        event_location_elem = event.find('div', class_=event_location_class)
        event_location = event_location_elem.text.strip() if event_location_elem else None

        image_elem = event.find('img', class_=image_url_class)
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

# URLs and classes for scraping
ticketmaster_url = 'https://www.ticketmaster.ca/discover/concerts/montreal'
ticketmaster_event_class = 'Flex-sc-145abwg-0'
ticketmaster_name_class = 'sc-fFeiMQ bCvzDL text text--dark text--primary sc-6jnhqk-0 kGOLzf event-tile__title'
ticketmaster_date_class = 'sc-fFeiMQ dBYlim text text--accent text--accent01 text-tm sc-17ev1tv-0 cnj20n-0 firocR iZsGLV event-tile__date-title'
ticketmaster_location_class = 'sc-fFeiMQ iIgzpz text text--dark text--secondary sc-1s3i3gy-0 hbRPym event-tile__sub-title'
ticketmaster_image_class = 'event-listing__thumbnail'

facebook_url = 'https://www.facebook.com/events/explore/montreal-quebec/102184499823699/'
facebook_event_class = 'x78zum5 x1n2onr6 xh8yej3'
facebook_name_class = None  # Add the correct class if available
facebook_date_class = None  # Add the correct class if available
facebook_location_class = None  # Add the correct class if available
facebook_image_class = 'x1rg5ohu x5yr21d xl1xv1r xh8yej3'

eventbrite_url = 'https://www.eventbrite.com/d/canada--montreal/events/'
eventbrite_event_class = 'Stack_root__1ksk7'
eventbrite_name_class = 'h2'
eventbrite_date_class = 'p'
eventbrite_location_class = 'Typography_root__487rx #585163 Typography_body-md__487rx event-card__clamp-line--one Typography_align-match-parent__487rx'
eventbrite_image_class = 'event-card-link'

# Scrape events from Ticketmaster
ticketmaster_events = scrape_events(ticketmaster_url, ticketmaster_event_class, ticketmaster_name_class,
                                     ticketmaster_date_class, ticketmaster_location_class, ticketmaster_image_class)

# Scrape events from Facebook
facebook_events = scrape_events(facebook_url, facebook_event_class, facebook_name_class,
                                facebook_date_class, facebook_location_class, facebook_image_class)

# Scrape events from Eventbrite
eventbrite_events = scrape_events(eventbrite_url, eventbrite_event_class, eventbrite_name_class,
                                   eventbrite_date_class, eventbrite_location_class, eventbrite_image_class)

# Combine all events
all_events = ticketmaster_events + facebook_events + eventbrite_events

# Convert the list of dictionaries to a JSON-formatted string
json_data = json.dumps(all_events, indent=2)

# Print or save the JSON data as needed
print(json_data)
