import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json

# 1. Pegar Conteúdo HTML a partir da URL
url = "https://www.ticketmaster.ca/search?sort=date&startDate=2024-01-18&endDate=2024-02-29"

option = Options()
option.headless = True
driver = webdriver.Chrome(options=option)

driver.get(url)
time.sleep(10)

driver.find_element_by_xpath(
    '//*[@id="pageInfo"]/div[2]/div/div[2]/div/ul').click()

driver.quit()
