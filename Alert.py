from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

try:

    driver.get("https://accounts.zoho.com/signin")
    time.sleep(2)


    title = driver.title


    if "Zoho" in title:
        message = "Site loaded: Zoho Login"
    elif "accounts" in title.lower():
        message = "Partial match: Contains 'accounts'"
    else:
        message = "Unexpected page title"


    driver.execute_script(f"alert('{message}');")
    time.sleep(5)
    driver.switch_to.alert.accept()

finally:
    driver.quit()
