from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyshorteners
import time

def pesquisarItem(driver, item):
    searchbar = driver.find_element(By.XPATH, '//*[@id="twotabsearchtextbox"]')
    searchbar.send_keys(f"{item}")
    searchbar.send_keys(Keys.ENTER)
    time.sleep(3)
    prices = driver.find_elements(By.CLASS_NAME, 'a-price-whole')
    fraction = driver.find_elements(By.CLASS_NAME, 'a-price-fraction')
    pricesList = []
    
    for i in range(5):
        try:
            price = prices[i].text
            price = str(price).replace('.', '')
        except:
            pass
        fullPrice = f'{price}.{fraction[i].text}'
        pricesList.append(float(fullPrice)) 
    return pricesList

def tratarDados(driver, pricesList):
    minValue = min(pricesList)
    indexValue = pricesList.index(minValue)
    titles = driver.find_elements(By.CSS_SELECTOR, 'h2 > a')
    titles[indexValue].click()

def coletaItem(driver):
    try:
        price = driver.find_elements(By.CLASS_NAME, 'a-price-whole')
        fraction = driver.find_elements(By.CLASS_NAME, 'a-price-fraction')
        fullPrice = f'{price[0].text}.{fraction[0].text}'
    except:
        fullPrice = driver.find_element(By.CSS_SELECTOR, '.apexPriceToPay:nth-child(1)').text
        fullPrice = fullPrice.replace('R$', '')

    title = driver.find_element(By.XPATH, '//*[@id="productTitle"]').text
    time.sleep(1)
    try:
        seller = driver.find_elements(By.CLASS_NAME, 'tabular-buybox-text-message')
        seller = seller[1].text
    except:
        try:
            seller = driver.find_element(By.ID, 'sellerProfileTriggerId').text
        except:
            seller = 'Amazon'
        
    url = driver.current_url
    shorturl = pyshorteners.Shortener().tinyurl.short(f"{url}")
    return(shorturl, title, fullPrice, seller)
