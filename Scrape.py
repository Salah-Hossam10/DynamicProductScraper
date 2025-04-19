# Import necessary libraries for web scraping and saving data
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import csv
import time

# Setup Chrome options to run in headless mode (no browser window pops up)
options = Options()
options.add_argument('--headless')  # Run browser in background
options.add_argument('--no-sandbox')  # Helps in Linux environments
options.add_argument('--disable-dev-shm-usage')  # Prevents memory issues

# Create Chrome browser using WebDriver Manager (automatically installs correct ChromeDriver)
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Set the starting URL of the website you want to scrape
url = "https://books.toscrape.com/catalogue/page-1.html"
browser.get(url)  # Open the website in the browser

# Prepare an empty list to store all product data
products = []

# Start a loop to go through all pages (pagination)
while True:
    time.sleep(2)  # Wait a little to make sure page loads (basic delay)

    # Get all product blocks on the page
    items = browser.find_elements(By.CLASS_NAME, "product_pod")

    # Loop through each product item
    for item in items:
        # Get the name of the book
        name = item.find_element(By.TAG_NAME, "h3").text

        # Get the link to the book's detail page
        link = item.find_element(By.TAG_NAME, "a").get_attribute("href")

        # Get the price text (e.g., "£53.74") and clean it
        price_raw = item.find_element(By.CLASS_NAME, "price_color").text
        price = float(price_raw.replace('£', '').strip())  # Remove pound sign and convert to float

        # Get the rating class (e.g., "star-rating Three")
        rating_class = item.find_element(By.CLASS_NAME, "star-rating").get_attribute("class")

        # Extract the actual rating word (e.g., "Three")
        rating_text = rating_class.split()[-1]

        # Convert rating word to number using a dictionary
        rating_dict = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
        rating = rating_dict.get(rating_text, None)  # Default to None if rating not found

        # Store all the collected data in a dictionary and add to the list
        products.append({
            "name": name,
            "price": price,
            "url": link,
            "rating": rating
        })

    # Try to go to the next page by clicking the "next" button
    try:
        next_button = browser.find_element(By.CLASS_NAME, "next")
        next_link = next_button.find_element(By.TAG_NAME, "a").get_attribute("href")
        browser.get(next_link)  # Load the next page
    except:
        break  # If there is no next button, end the loop

# After scraping is done, close the browser
browser.quit()

# Open a CSV file to save the product data
with open("products.csv", "w", newline="", encoding="utf-8") as f:
    # Define the column headers for the CSV
    writer = csv.DictWriter(f, fieldnames=["name", "price", "url", "rating"])
    writer.writeheader()  # Write the headers as the first row

    # Write each product as a row in the CSV file
    for product in products:
        writer.writerow(product)
