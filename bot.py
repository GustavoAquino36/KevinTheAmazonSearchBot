from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from OpenBrowser import OpenBrowser
from lerXLSX import LerConfig
from funcSite import pesquisarItem, tratarDados
import time
import os
import sys

dictConfig = LerConfig()
item = input("Qual item deseja pesquisar via Amazon?\n")
driver = OpenBrowser("https://www.amazon.com.br")
lista = pesquisarItem(driver, item)
tratarDados(driver, lista)