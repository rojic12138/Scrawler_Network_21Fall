from selenium import webdriver
from random import randint
import time

url = "https://reddit.com/hot"

driver = webdriver.Firefox()
driver.get(url)

# Scroll Limit
scroll_limit = 20

# First Scroll
last_height = driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
scroll_count = 0

while True:
    # Control variables
    scroll_count += 1
    scroll_pause_time_c = randint(3, 8)

    # Wait
    wait = time.sleep(scroll_pause_time_c)
    print('\nScroll Number: ', scroll_count)
    print('WAIT TIME: ', scroll_pause_time_c, ' s')
    print("SCROLLING NOW")

    # scroll to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # Set New Height
    new_height = driver.execute_script("return document.body.scrollHeight")

    # Check if bottom reached or limit reached
    if new_height == last_height or scroll_count == scroll_limit:
        with open('reddit_dump.dat', 'w', encoding="UTF-8") as dump:
            dump.writelines(driver.page_source)
        break
    last_height = new_height

driver.close()