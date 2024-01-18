import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json

# 1. Pegar Conteúdo HTML a partir da URL
url = "https://www.ticketmaster.ca/discover/concerts/montreal"

option = Options()
option.headless = True
driver = webdriver.Chrome()

driver.get(url)

driver.quit()

time.sleep(10)
