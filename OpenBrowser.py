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
      service = Service(driverpath)
      service.start()
      driver = webdriver.Chrome(service=service(ChromeDriverManager.install()), options=options)
      driver.get(site)
  except Exception as expt:
    print(f"Erro: {expt}")
  return driver