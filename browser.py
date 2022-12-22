from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

service = ChromeService(ChromeDriverManager(
    chrome_type=ChromeType.CHROMIUM).install())

driver = webdriver.Chrome(service=service)

driver.get("http://selenium.dev")

driver.quit()
