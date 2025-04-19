# Web Scraping & Data Processing Task

## Overview
This project is a Python-based web scraper that collects product information from a dynamic JavaScript-powered site — [books.toscrape.com](http://books.toscrape.com). It uses **Selenium** with **headless Chrome** to simulate browser behavior, navigate through all pages, extract relevant product details, clean the data, and store it in a CSV file.

The scraper collects:
- Product Name
- Price (float)
- Product URL
- Rating (integer from 1 to 5)

## Setup

- Clone the repo:
  ```bash
  git clone https://github.com/your-username/toscrape-books-selenium.git
  cd toscrape-books-selenium
Create and activate a virtual environment:
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

Install dependencies:
pip install -r requirements.txt

Usage
python scrape.py

Output will be saved as:
products.csv (containing structured product data)

Notes
The website (books.toscrape.com) is static in design but was scraped using Selenium to demonstrate browser automation.
Basic time.sleep() is used for delay, which can be improved with smart waits.
Ratings were mapped from words ("Three") to numbers (3) using a dictionary.
All price symbols (like £) were removed and converted to float.
The script gracefully handles pagination until no "next" button is found.


Future Improvements
Use WebDriverWait instead of static time.sleep()
Add CLI arguments for dynamic URL and output file options
Export to multiple formats: JSON, SQLite, etc.
Implement error handling and retry logic
