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
    titles = driver.find_elements(By.CSS_SELECTOR, 'h2.s-line-clamp-4 > a')
    titles[indexValue].click()

def coletaItem(driver):
    price = driver.find_elements(By.CLASS_NAME, 'a-price-whole')
    fraction = driver.find_elements(By.CLASS_NAME, 'a-price-fraction')
    fullPrice = f'{price[0].text}.{fraction[0].text}'
    time.sleep(1)
    title = driver.find_element(By.XPATH, '//*[@id="productTitle"]').text
    time.sleep(1)
    try:
        seller = driver.find_element(By.ID, 'sellerProfileTriggerId').text
    except:
        seller = driver.find_element(By.XPATH, '//*[@id="tabular-buybox"]/div[1]/div[6]/div/span').text
    url = driver.current_url
    shorturl = pyshorteners.Shortener().tinyurl.short(f"{url}")
    print(f'''--------------- Item com menor preço encontrado -------------------\n
    URL do Site: {shorturl}
    Nome do Item encontrado: {title}
    Preço do item: {fullPrice}
    Vendido por: {seller}''')