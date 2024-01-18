import asyncio
from pyppeteer import launch
from bs4 import BeautifulSoup

async def main():
    url = 'https://ra.co/events/ca/montreal'

    browser = await launch(headless=True)
    page = await browser.newPage()
    await page.goto(url)

    # Wait for the page to load (you can adjust the wait time accordingly)
    await page.waitFor(10000)

    page_content = await page.content()
    webpage = BeautifulSoup(page_content, 'html.parser')

    print(webpage)

    events = webpage.find_all('div', class_='Box-omzyfs-0 guLsXx')

    # Rest of your code for processing events

    await browser.close()

# Run the event loop
asyncio.get_event_loop().run_until_complete(main())

# Rest of your code for processing events


# for event in events:

# driver.quit()
