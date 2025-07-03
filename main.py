import time
import os
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import openpyxl


os.makedirs("screenshots", exist_ok=True)
os.makedirs("reports", exist_ok=True)


log_path = "reports/zoho_login.log"
logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logging.info("=== Zoho Login Automation Started ===")


excel_path = "reports/zoho_login.xlsx"
wb = openpyxl.Workbook()
sheet = wb.active
sheet.append(["Step", "Status", "Screenshot"])


html_path = "reports/zoho_login.html"
html_file = open(html_path, "w")
html_file.write("<html><head><title>Zoho Login Report</title></head><body><h2>Zoho Login Test</h2><table border='1'>")
html_file.write("<tr><th>Step</th><th>Status</th><th>Screenshot</th></tr>")

def capture(step_name):
    filename = f"screenshots/{step_name}.png"
    driver.save_screenshot(filename)
    logging.info(f"📸 Screenshot: {filename}")
    sheet.append([step_name, "PASS", filename])
    html_file.write(f"<tr><td>{step_name}</td><td>PASS</td><td><img src='../{filename}' width='200'></td></tr>")

def log_fail(step_name, error):
    filename = f"screenshots/{step_name}_error.png"
    driver.save_screenshot(filename)
    logging.error(f"❌ {step_name} failed: {error}")
    sheet.append([step_name, "FAIL", filename])
    html_file.write(f"<tr><td>{step_name}</td><td>FAIL</td><td><img src='../{filename}' width='200'></td></tr>")


options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:

    logging.info("Opening Zoho login page...")
    driver.get("https://accounts.zoho.com/signin")
    time.sleep(2)
    capture("login_page")


    email_field = driver.find_element(By.ID, "login_id")
    email_field.send_keys("adithyas.csbs2022@citchennai.net")
    time.sleep(1)


    driver.find_element(By.ID, "nextbtn").click()
    logging.info("Email entered")
    time.sleep(2)


    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("welcometocit_04")
    time.sleep(1)


    driver.find_element(By.ID, "nextbtn").click()
    time.sleep(3)
    capture("dashboard_or_post_login")

except Exception as e:
    log_fail("login_process", str(e))

finally:
    driver.quit()
    logging.info("Browser closed")


    wb.save(excel_path)
    html_file.write("</table></body></html>")
    html_file.close()

    logging.info(f"Excel report saved: {excel_path}")
    logging.info(f"HTML report saved: {html_path}")
    logging.info("=== Zoho Login Automation Completed ===")
