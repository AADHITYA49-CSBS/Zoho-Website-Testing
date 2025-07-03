# Zoho-Website-Testing (Selenium + Python)
 
Automation scripts for Zoho login using Selenium.

This project automates login testing for [Zoho Accounts](https://accounts.zoho.com/signin) using Selenium WebDriver in Python.

## 🔍 Scripts Included

- `zoho_alert_test.py` – Verifies page title with JavaScript alert
- `zoho_login_report.py` – Automates full login + generates:
  - Screenshots
  - Excel report
  - HTML report
  - Log file

## 📂 Folder Structure

pythonProject/
├── zoho_login_report.py
├── zoho_alert_test.py
├── Test Plan - Zoho Login Automation.docx
├── reports/
│ ├── zoho_login.xlsx
│ ├── zoho_login.html
│ └── zoho_login.log
├── screenshots/
│ └── login_page.png
├── README.md
└── .gitignore


## ✅ Requirements

- Python 3.10+
- `selenium`
- `openpyxl`
- `webdriver-manager`

Install with:

```bash
pip install selenium openpyxl webdriver-manager


