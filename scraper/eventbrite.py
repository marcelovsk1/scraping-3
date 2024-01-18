# from bs4 import BeautifulSoup
# import requests

# page = requests.get('https://www.eventbrite.com/d/canada--montreal/events/')
# webpage = BeautifulSoup(page.content, 'html.parser')

# events = webpage.find_all('div', attrs={'class': 'Stack_root__1ksk7'})

# for event in events:
#     event_name = event.find('h2').text
#     event_date = event.find('p').text.strip()
#     event_location = event.find('p', class_='Typography_root__487rx #585163 Typography_body-md__487rx event-card__clamp-line--one Typography_align-match-parent__487rx').text.strip()
#     event_image = event.find('a', class_='event-card-link')

#     image_url = event_image['href'] if event_image else None

#     print(f"{event_name}")
#     print(f"{event_date}")
#     print(f"{event_location}")
#     print(f"Image URL: {image_url}")
#     print("=" * 100)


# JSON
from bs4 import BeautifulSoup
import requests
import json

page = requests.get('https://www.eventbrite.com/d/canada--montreal/events/')
webpage = BeautifulSoup(page.content, 'html.parser')

events = webpage.find_all('div', attrs={'class': 'Stack_root__1ksk7'})

event_list = []

for event in events:
    event_name = event.find('h2').text if event.find('h2') else None
    event_date = event.find('p').text.strip() if event.find('p') else None
    event_location_element = event.find('p', class_='Typography_root__487rx #585163 Typography_body-md__487rx event-card__clamp-line--one Typography_align-match-parent__487rx')
    event_location = event_location_element.text.strip() if event_location_element else None
    event_image = event.find('a', class_='event-card-link')
    image_url = event_image['href'] if event_image else None

    event_dict = {
        'event': event_name,
        'date': event_date,
        'location': event_location,
        'image_url': image_url
    }

    event_list.append(event_dict)

events_json = json.dumps(event_list, indent=2, ensure_ascii=False)

print(events_json)
