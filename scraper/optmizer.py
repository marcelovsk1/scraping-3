import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

def scrape_events(url, event_class):
    options = Options()
    options.headless = True

    driver = webdriver.Chrome(options=options)
    driver.get(url)
    driver.implicitly_wait(10)

    page_content = driver.page_source
    webpage = BeautifulSoup(page_content, 'html.parser')

    events = webpage.find_all('div', class_=event_class)

    event_list = []

    for event in events:
        event_name_elem = event.find('span', class_='sc-fyofxi-5 gJmuwa')
        event_name = event_name_elem.text if event_name_elem else None

        event_month_elem = event.find('div', class_='sc-1evs0j0-1 gwWuEQ')
        event_month = event_month_elem.text.strip() if event_month_elem else None

        event_day_elem = event.find('div', class_='sc-1evs0j0-2 ftHsmv')
        event_day = event_day_elem.text.strip() if event_day_elem else None

        event_location_elem = event.find('span', class_='sc-fyofxi-7 PpnvD')
        event_location = event_location_elem.text.strip() if event_location_elem else None

        event_info = {
            'Event Name': event_name,
            'Event Month': event_month,
            'Event Day': event_day,
            'Event Location': event_location
        }

        event_list.append(event_info)

    driver.quit()

    return event_list

# Rest of your code remains unchanged


# URL para o primeiro site
eventbrite_url = 'https://www.eventbrite.com/d/canada--montreal/events/'
eventbrite_event_class = 'Stack_root__1ksk7'

# URL para o segundo site
ticketmaster_url = 'https://www.ticketmaster.ca/search?sort=date&startDate=2024-01-18&endDate=2024-02-29'
ticketmaster_event_class = 'sc-fyofxi-0 MDVIb'

# Scraping dos eventos do Eventbrite
eventbrite_events = scrape_events(eventbrite_url, eventbrite_event_class)

# Scraping dos eventos do Ticketmaster
ticketmaster_events = scrape_events(ticketmaster_url, ticketmaster_event_class)

# Unindo as listas de eventos
all_events = eventbrite_events + ticketmaster_events

# Convertendo a lista de eventos para JSON
json_data = json.dumps(all_events, indent=2)

# Imprimindo o JSON resultante
print(json_data)
