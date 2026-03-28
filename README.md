# Job Scraper with Selenium

This project is a Python script that uses Selenium to automate job searching and filtering on the InfoJobs website and saves the collected job links into an Excel spreadsheet.

---

## Features

- Automates opening the InfoJobs website
- Automatically accepts the cookie consent banner
- Applies filters for jobs in the Information Technology and Telecommunications fields
- Filters internship-level positions
- Captures links from job listings on the page
- Saves collected links into an Excel spreadsheet (`vagas.xlsx`)
- Includes a wait time to ensure data loads before saving
- (Optional) Allows saving the spreadsheet to a specific folder on the desktop

---

## Technologies Used

- Python
- Selenium
- Pandas

---

# Legal Notice

## This project is for educational purposes only.

- Does not collect personal or sensitive data
- Does not bypass captcha, authentication, or other security measures
- All collected data is public and accessible without login
- Usage must comply with InfoJobs Terms of Service
- Do not use this script for commercial or large-scale purposes without permission

---

# Project Objective

This project was created as practice for:

- Task automation with Selenium
- Public web data extraction
- Data structuring with pandas
- Spreadsheet generation with Python

---

## How to Use

1. Install the required dependencies:

```bash
pip install -r requirements.txt
```

2. Download the ChromeDriver compatible with your Google Chrome version and place it in your PATH or in the same folder as the script.
3. Clone this repository or copy the script to your machine.
4. Run the script:

```bash
python app.py
```

After execution, a `vagas.xlsx` file will be created in the project folder (or in the configured folder in the script).

---

## How It Works

- The script opens the Chrome browser and accesses the InfoJobs job listings page for the selected region (default is Rio de Janeiro).
- Automatically accepts the cookie consent.
- Applies filters to show IT internship-level positions.
- Collects job listing links displayed on the page.
- Saves the links into an Excel file, avoiding duplicates.
- Closes the browser after saving the spreadsheet.

---

## Customization

You can adjust filters for other fields or job levels by modifying the selectors in the code. You can also change where the spreadsheet is saved by modifying the `salvar_planilha` function.

---

## Notes

- ChromeDriver must be installed and compatible with your Chrome browser version.
- If InfoJobs changes its layout or selectors, the script may need updates.
- This script is a starting point for automated job scraping and can be expanded to extract additional job information.
