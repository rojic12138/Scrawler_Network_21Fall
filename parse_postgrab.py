from bs4 import BeautifulSoup as bs

def get_soup_from_file(file):
    with open(file, 'r', encoding="UTF-8") as f:
        soup = bs(f, 'html.parser')
    return soup

def print_all(soup, test_id):
    with open('test.dat', 'w', encoding="UTF-8") as f:
        sub = soup.find_all(attrs={'data-click-id' : test_id})
        f.writelines([str(a) + '\n' for a in sub])



def write_posts(soup):

    subreddits = soup.find_all(attrs={'data-click-id' : 'subreddit'})
    timestamps = soup.find_all(attrs={'data-click-id' : 'timestamp'})
    posts = soup.find_all('a', attrs={'data-click-id' : 'body'})
    comments = soup.find_all(attrs={'data-click-id' : 'comments'})

    f = open('reddit_dump_parse.dat', 'w', encoding="utf-8")
    
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
    soup = get_soup_from_file("reddit_dump.dat")
    
    print_all(soup, 'body')
    write_posts(soup)
        




if __name__ == "__main__":
    main()