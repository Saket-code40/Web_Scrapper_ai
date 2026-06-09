from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def scrape_website(website_url):
    options = Options()
    options.binary_location = "/usr/bin/google-chrome"

    driver = webdriver.Chrome(options=options)

    try:
        driver.get(website_url)
        time.sleep(10)
        return driver.page_source
    finally:
        driver.quit()