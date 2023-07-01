from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from OpenBrowser import OpenBrowser
from lerXLSX import LerConfig
import time
import os
import sys

dictConfig = LerConfig()
item = input("Qual item deseja pesquisar via Amazon?\n")
driver = OpenBrowser("https://www.amazon.com.br")

def pesquisarItem(item):
    searchbar = driver.find_element(By.XPATH, '//*[@id="twotabsearchtextbox"]')
    searchbar.send_keys(f"{item}")
    searchbar.send_keys(Keys.ENTER)
    time.sleep(1)
    prices = driver.find_elements(By.CLASS_NAME, 'a-price-whole')
    fraction = driver.find_elements(By.CLASS_NAME, 'a-price-fraction')
    pricesList = []
    for i in range(5):
        fullPrice = f'{prices[i].text},{fraction[i].text}'
        pricesList.append(fullPrice) 
    return pricesList