from bs4 import BeautifulSoup as bs
from bs4 import SoupStrainer
import re
import requests


def get_page(url):

    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br"
    }       

    start_page = requests.get(url, headers=header)
    if start_page.status_code != 200:
        return None
    
    # Infinite Scrolling response: TBD
    # I'm thinking either selenium or maybe try again with requests.
    # most likely should use selenium

    only_subreddits = SoupStrainer(href=re.compile("/r/"))

    soup = bs(start_page.content, 'html.parser', parse_only=only_subreddits)
    return soup


def write_post(soup):

    subreddits = soup.find_all(attrs={'data-click-id' : 'subreddit'})
    timestamps = soup.find_all(attrs={'data-click-id' : 'timestamp'})
    posts = soup.find_all(attrs={'data-click-id' : 'body'})
    comments = soup.find_all(attrs={'data-click-id' : 'comments'})

    f = open('dump.dat', 'w', encoding="utf-8")
    
    for i in range(len(posts)):
        f.write('Link: https://www.reddit.com' + posts[i]['href'] + '\n')
        f.write('Subreddit: ' + subreddits[i]['href'] + '\n')
        f.write('Timestamp: ' + timestamps[i].text + '\n')
        f.write('Post: ' + posts[i].text + '\n')
        f.write('Comments: ' + comments[i].text + '\n')
        f.write('\n')

    # for link in soup:
    #     if link.has_attr('href'):
    #         f.write(link['href'])
    #         f.write('\n')

    f.close()

def main():
    url = "https://www.reddit.com/hot/"
    soup = get_page(url)
    write_post(soup)


if __name__ == "__main__":
    main()