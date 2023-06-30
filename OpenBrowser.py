from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def OpenBrowser (driverpath, site):
  try:
      options = Options()

      options.add_argument("--log-level=2")
      options.add_argument("--start-maximized")
      options.add_experimental_option("detach", True)

      driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
      driver.get(site)
      return driver
  except Exception as expt:
    print(f"Erro: {expt}")