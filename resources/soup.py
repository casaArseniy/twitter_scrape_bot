import os
from bs4 import BeautifulSoup
from resources.scrapper_classes.post import Post
import sys

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
            return soup
    else:
        sys.exit("No html file found!")

    


def get_OP_soup():
    soup = get_soup()
    cards = soup.find_all('div', class_='css-175oi2r r-1iusvr4 r-16y2uox r-1777fci r-kzbkwu')
    posts = []
    for c in cards:
        message = c.find('div', class_='css-1rynq56 r-8akbws r-krxsd3 r-dnmrzs r-1udh08x r-bcqeeo r-qvutc0 r-37j5jr r-a023e6 r-rjixqe r-16dba41 r-bnwqim')
        tag = c.find('div', class_='css-1rynq56 r-dnmrzs r-1udh08x r-3s2u2q r-bcqeeo r-qvutc0 r-37j5jr r-a023e6 r-rjixqe r-16dba41 r-18u37iz r-1wvb978')
        date = c.find('div', class_='css-175oi2r r-18u37iz r-1q142lx')
        stats = c.find_all('span', attrs={'data-testid': 'app-text-transition-container'})

        if tag is None or date is None:
            continue

        if message is None:
            message_text = ''
        else:
            message_text = message.text

        num_reply = 0
        if stats[0].text!='':
            num_reply=int(stats[0].text)

        url_element = c.find('a', class_='css-1rynq56 r-bcqeeo r-qvutc0 r-37j5jr r-a023e6 r-rjixqe r-16dba41 r-xoduu5 r-1q142lx r-1w6e6rj r-9aw3ui r-3s2u2q r-1loqt21')

        posts.append(Post(tag.text, date.text, message_text, num_reply, "https://twitter.com" + url_element.get('href')))
    return posts

def get_COMMENTER_soup():
    soup = get_soup()
    cards = soup.find_all('div', {'data-testid': 'cellInnerDiv'})
    posts = []
    signal = 0
    for c in cards[1:]:

        #show more replies
        if c.find('div', class_ = 'css-1rynq56 r-bcqeeo r-qvutc0 r-37j5jr r-q4m81j r-a023e6 r-rjixqe r-16dba41'):
            signal = 1
            break
        # discover more
        if c.find('div', class_ = 'css-175oi2r r-k200y r-z80fyv r-1777fci'):
            signal = 1
            break
        
        try:
            message = c.find('div', class_='css-1rynq56 r-8akbws r-krxsd3 r-dnmrzs r-1udh08x r-bcqeeo r-qvutc0 r-37j5jr r-a023e6 r-rjixqe r-16dba41 r-bnwqim')
            if message is None:
                message_text = ''
            else:
                message_text = message.text
            tag = c.find('div', class_='css-1rynq56 r-dnmrzs r-1udh08x r-3s2u2q r-bcqeeo r-qvutc0 r-37j5jr r-a023e6 r-rjixqe r-16dba41 r-18u37iz r-1wvb978')
            date = c.find('div', class_='css-175oi2r r-18u37iz r-1q142lx')

            stats = c.find_all('span', attrs={'data-testid': 'app-text-transition-container'})
            # for s in stats:
            #     print(s.text)
            num_reply = 0
            if stats[0].text!='':
                num_reply=int(stats[0].text)

            url_element = c.find('a', class_='css-1rynq56 r-bcqeeo r-qvutc0 r-37j5jr r-a023e6 r-rjixqe r-16dba41 r-xoduu5 r-1q142lx r-1w6e6rj r-9aw3ui r-3s2u2q r-1loqt21')

            posts.append(Post(tag.text, date.text, message_text, num_reply, 'https://twitter.com' + url_element.get('href')))
        except:
            continue

    return posts, signal

def get_REPLY_name_tags():
    soup = get_soup()
    cards = soup.find_all('div', {'data-testid': 'cellInnerDiv'})
    name_tags = []

    for c in cards[1:]:

        #show more replies
        if c.find('div', class_ = 'css-1rynq56 r-bcqeeo r-qvutc0 r-37j5jr r-q4m81j r-a023e6 r-rjixqe r-16dba41'):
            signal = 1
            break
        # discover more
        if c.find('div', class_ = 'css-175oi2r r-k200y r-z80fyv r-1777fci'):
            signal = 1
            break
        
        try:
            tag = c.find('div', class_='css-1rynq56 r-dnmrzs r-1udh08x r-3s2u2q r-bcqeeo r-qvutc0 r-37j5jr r-a023e6 r-rjixqe r-16dba41 r-18u37iz r-1wvb978')
            name_tags+=tag.text
        except:
            continue

        return name_tags, signal