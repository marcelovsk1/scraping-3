from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

url = 'https://www.facebook.com/events/explore/montreal-quebec/102184499823699/'

options = Options()
options.headless = True

driver = webdriver.Chrome(options=options)
driver.get(url)

# Aguarde alguns segundos para garantir que a página seja totalmente carregada
driver.implicitly_wait(10)

# Obtenha o conteúdo da página após a execução do JavaScript
page_content = driver.page_source

# Use o BeautifulSoup para analisar o conteúdo
webpage = BeautifulSoup(page_content, 'html.parser')

# Encontre os eventos usando a classe apropriada ou outras características únicas
events = webpage.find_all('div', class_='x78zum5 x1n2onr6 xh8yej3')

# Imprima os eventos encontrados
for event in events:
    print(event.text)

# Feche o navegador
driver.quit()
















# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

# # 1. Pegar Conteúdo HTML a partir da URL
# url = "https://www.facebook.com/events/explore/montreal-quebec/102184499823699/"

# option = Options()
# option.headless = True
# driver = webdriver.Chrome(options=option)

# driver.get(url)
# time.sleep(10)

# # Aguardar até 10 segundos até que o elemento esteja presente na página
# driver.implicitly_wait(10)

# # Clicar no elemento usando XPath
# driver.find_element_by_xpath(
#     '//*[@id="mount_0_0_m8"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[3]/div[1]/div'
# ).click()

# driver.quit()
