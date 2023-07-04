from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from OpenBrowser import OpenBrowser
from lerXLSX import LerConfig
from funcSite import pesquisarItem, tratarDados, coletaItem
from sendEmail import stringfyMessage, sendEmail

dictConfig = LerConfig()
item = input("Qual item deseja pesquisar via Amazon?\n")
email = input("Qual email deseja enviar os resultados?\n")
driver = OpenBrowser("https://www.amazon.com.br")
lista = pesquisarItem(driver, item)
tratarDados(driver, lista)
shorturl, title, fullPrice, seller = coletaItem(driver)
message = stringfyMessage(item, lista, shorturl, title, fullPrice, seller)
driver.quit()
sendEmail(message, email)