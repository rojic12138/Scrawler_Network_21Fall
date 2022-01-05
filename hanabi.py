# Twitter Parsing
# proof of concept only

from selenium import webdriver
from bs4 import BeautifulSoup as bs
from random import randint
import time

# Goes to URL and scrolls to scroll limit then dumps page in .dat file
def scroll_and_grab(url, dump_file = "dump.dat", scroll_limit = 5):

    driver = webdriver.Firefox()
    driver.get(url)
    scroll_count = 0

    while True:
        # Control variables
        scroll_count += 1
        scroll_pause_time_c = randint(3, 8)

        # Wait
        time.sleep(scroll_pause_time_c)
        print('\nScroll Number: ', scroll_count)
        print('WAIT TIME: ', scroll_pause_time_c, 's')
        print("SCROLLING NOW")

        # scroll to bottom
        new_height = "window.scrollTo(0, " + str(scroll_count) + "*window.innerHeight)"
        driver.execute_script(new_height)

        # Check if bottom reached or limit reached
        if scroll_count == scroll_limit:
            break

        # print out page_source
        soup = bs(driver.page_source, 'html.parser')

        with open(dump_file, 'a', encoding="UTF-8") as dump:
            dump.writelines([str(span.text) + '\n' for span in soup.find_all('span')])

    driver.close()


def get_query(query):
    url = "https://twitter.com/search?q=" + query + "&src=typed_query&f=top"
    scroll_and_grab(url, dump_file="hanabi_query.dat")


def get_user(user):
    url = "https://twitter.com/" + user
    scroll_and_grab(url, dump_file="hanabi_user.dat")


def prune_file(file):
    with open(file, 'r', encoding="utf-8") as read:
        lines = read.readlines()
    with open(file, 'w', encoding="utf-8") as write:
        for i in range(len(lines) - 1):
            if lines[i].strip() != lines[i+1].strip():
                write.write(lines[i])


def main():
    # Twitter is also AJAX
    get_user("PKU1898")
    

if __name__ == "__main__":
    main()