import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

def scrape_events(url, event, event_name, event_date, event_location, image_url):
    options = Options()
    options.headless = True

    driver = webdriver.Chrome(options=options)
    driver.get(url)
    driver.implicitly_wait(10)

    page_content = driver.page_source
    webpage = BeautifulSoup(page_content, 'html.parser')

    events = webpage.find_all('div', class_=event)

    event_list = []

    for event in events:
        event_name_elem = event.find('span', class_=event_name)
        event_name = event_name_elem.text if event_name_elem else None

        event_date_elem = event.find('div', class_=event_date)
        event_date = event_date_elem.text.strip() if event_date_elem else None

        event_location_elem = event.find('span', class_=event_location)
        event_location = event_location_elem.text.strip() if event_location_elem else None

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

# URLs
eventbrite_url = 'https://www.eventbrite.com/d/canada--montreal/events/'
eventbrite_event = 'Stack_root__1ksk7'
eventbrite_name = 'h2'
eventbrite_date = 'p'
eventbrite_location = 'Typography_root__487rx #585163 Typography_body-md__487rx event-card__clamp-line--one Typography_align-match-parent__487rx'
eventbrite_image = 'event-card-link'

ticketmaster_url = 'https://www.ticketmaster.ca/search?sort=date&startDate=2024-01-18&endDate=2024-02-29'
ticketmaster_event = 'sc-fyofxi-0 MDVIb'
ticketmaster_name = 'sc-fyofxi-5 gJmuwa'
ticketmaster_date = 'sc-1evs0j0-1 gwWuEQ'
ticketmaster_location = 'sc-fyofxi-7 PpnvD'

facebook_url = 'https://www.facebook.com/events/explore/montreal-quebec/102184499823699/'
facebook_event = 'x78zum5 x1n2onr6 xh8yej3'
facebook_image = 'x1rg5ohu x5yr21d xl1xv1r xh8yej3'

# Eventbrite
eventbrite_events = scrape_events(eventbrite_url, eventbrite_event, eventbrite_name,
                                  eventbrite_date, eventbrite_location, eventbrite_image)

# Ticketmaster
ticketmaster_events = scrape_events(ticketmaster_url, ticketmaster_event, ticketmaster_name,
                                    ticketmaster_date, ticketmaster_location, image_url_class=None)

# Facebook
facebook_events = scrape_events(facebook_url, facebook_event, event_name_class=None,
                                event_date_class=None, event_location_class=None, image_url_class=facebook_image)

# Events List
all_events = eventbrite_events + ticketmaster_events + facebook_events

json_data = json.dumps(all_events, indent=2)

print(json_data)
