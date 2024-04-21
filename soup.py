import os
from bs4 import BeautifulSoup
import requests

class Post:
    def __init__(self, name_tag, post_date, message, num_replies, url):
        self.name_tag = name_tag
        self.post_date = post_date
        self.message = message
        self.num_replies = num_replies
        self.url = url
    def __str__(self):
        return f"{self.name_tag}, date: {self.post_date} \nmessage: {self.message}\nurl:{self.url}\nreplies: {self.num_replies}\n"


def get_soup():
    current_directory = os.getcwd()

    # List all files in the directory
    files = os.listdir(current_directory)

    # Filter HTML files
    html_files = [file for file in files if file.endswith('.html')]

    if html_files:
        # Assuming there's only one HTML file in the directory, you can select the first one
        html_doc = os.path.join(current_directory, html_files[0])

        with open(html_doc, 'r', encoding='utf-8') as html_file:
            # Create a BeautifulSoup object
            soup = BeautifulSoup(html_file, 'html.parser')

    cards = soup.find_all('div', class_='css-175oi2r r-1iusvr4 r-16y2uox r-1777fci r-kzbkwu')

    posts = []

    for c in cards:
        message = c.find('div', class_='css-1rynq56 r-8akbws r-krxsd3 r-dnmrzs r-1udh08x r-bcqeeo r-qvutc0 r-37j5jr r-a023e6 r-rjixqe r-16dba41 r-bnwqim')
        name_at_date = c.find('div', class_='css-175oi2r r-1wbh5a2 r-dnmrzs r-1ny4l3l r-1awozwy r-18u37iz')
        tag = c.find('div', class_='css-1rynq56 r-dnmrzs r-1udh08x r-3s2u2q r-bcqeeo r-qvutc0 r-37j5jr r-a023e6 r-rjixqe r-16dba41 r-18u37iz r-1wvb978')
        date = c.find('div', class_='css-175oi2r r-18u37iz r-1q142lx')

        stats = c.find_all('span', attrs={'data-testid': 'app-text-transition-container'})
        num_reply = 0
        if stats[0].text!='':
            num_reply=int(stats[0].text)

        url_element = c.find('a', class_='css-1rynq56 r-bcqeeo r-qvutc0 r-37j5jr r-a023e6 r-rjixqe r-16dba41 r-xoduu5 r-1q142lx r-1w6e6rj r-9aw3ui r-3s2u2q r-1loqt21')

        posts.append(Post(tag.text, date.text, message.text, num_reply, "https://twitter.com" + url_element.get('href')))
        
        # print(tag.text)
        # print(date.text)
        # print(message.text) # empty space is image only
        # print(stats[0].text)
        # print(url_element.get('href'))

    return posts
