import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

Zillow_url = "https://appbrewery.github.io/Zillow-Clone/"

CHROME_OPTION = webdriver.ChromeOptions()
CHROME_OPTION.add_experimental_option("detach", True)

response = requests.get(Zillow_url)
zillow_data = response.text
links_list = []
prices_list = []
addresses_list = []

soup = BeautifulSoup(zillow_data, "html.parser")

links_div = soup.find_all('div', class_='StyledPropertyCardDataWrapper')
prices = soup.find_all('span', class_='PropertyCardWrapper__StyledPriceLine')
addresses = soup.find_all('address')

for price in prices:
    prices_list.append(price.text[0:6])

for address in addresses:
    addresses_list.append(address.text.strip())

for div in links_div:
    a_tag = div.find('a')
    if a_tag and 'href' in a_tag.attrs:
        link = a_tag['href']
        links_list.append(link)

driver = webdriver.Chrome(options=CHROME_OPTION)
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSf9_33g-gzltU5718wWao_ApifjI5gORszrC57Mhc29a3r2bA/viewform?usp"
           "=sf_link")

time.sleep(3)

for i in range(len(links_list)):
    first_question = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div['
                                                   '1]/div/div[1]/input')

    first_question.send_keys(addresses_list[i])

    time.sleep(1)

    second_question = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div['
                                                    '1]/div/div[1]/input')
    second_question.send_keys(prices_list[i])

    time.sleep(1)

    third_question = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div['
                                                   '1]/div/div[1]/input')
    third_question.send_keys(links_list[i])

    time.sleep(1)

    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    submit_button.click()

    time.sleep(2)
    another_response = driver.find_element(By.LINK_TEXT, 'ሌላ ምላሽ አስገባ')
    another_response.click()
    time.sleep(2)
