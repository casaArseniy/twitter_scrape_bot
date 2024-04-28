from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from soup import get_OP_soup, get_COMMENTER_soup
from table import *    

class Scrapper():

    OP_POSTS = []
    COMMENTER_POSTS = []
    REPLY_POSTS = []

    df_OP = create_Table()
    df_COMM = create_Table()
    # df_REPLY = create_Table()

    driver = webdriver.Chrome()

    def go_to(self, html):
        self.driver.get(html)
    
    def clear_data(self):
        self.OP_POSTS = []
        self.COMMENTER_POSTS = []
        self.REPLY_POSTS = []

        self.df_OP = create_Table()
        self.df_COMM = create_Table()

    
    def login(self, ID, PASSWORD):
        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(3)
        # Find the input element by class name
        input_element = self.driver.find_element(By.CLASS_NAME, 'r-30o5oe')
        # Input text into the element
        input_element.send_keys(ID)
        input_element.send_keys(Keys.ENTER)
        time.sleep(3)
        input_element = self.driver.find_element(By.NAME, 'password')
        input_element.send_keys(PASSWORD)
        input_element.send_keys(Keys.ENTER)
    
    def get_OP_posts(self, scroll_number):

        for i in range(scroll_number):  # Scroll down N times, adjust as needed
            html_content = self.driver.page_source
            time.sleep(1)
            with open("page.html", "w", encoding="utf-8") as f:
                f.write(html_content)
            self.OP_POSTS += get_OP_soup()
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)  # Wait for 2 seconds after each scroll
        
        html = self.driver.current_url
        # return posts, html
        return html
    
    def get_COMMENTER_posts(self, OP_PST):

        posts = []
        signal = 0
        index = 0
        html = OP_PST.url

        self.driver.get(html)
        time.sleep(1)

        while (signal == 0 and signal<2):  # Scroll down N times, adjust as needed
            html_content = self.driver.page_source
            with open("page.html", "w", encoding="utf-8") as f:
                f.write(html_content)
            pst, signal = get_COMMENTER_soup()
            OP_PST.comments += pst
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)  # Wait for 2 seconds after each scroll
            index +=1

        # self.COMMENTER_POSTS.append(posts)

        # return posts, html
        return html
    
    def access_OP_posts(self, scroll_number):
        html = self.get_OP_posts(scroll_number)
        for pst in self.OP_POSTS:
            self.df_OP = insert_post_into_Table(self.df_OP, html, pst)
    
    def access_COMMENTER_posts(self):
        for post in self.OP_POSTS:
            html = self.get_COMMENTER_posts(post)
            for pst in post.comments:
                self.df_COMM = insert_post_into_Table(self.df_COMM, html, pst)
    
    def save_data(self):
        table_to_csv(self.df_OP, 'OP')
        table_to_csv(self.df_COMM, 'COMMENTER')
    
    def close(self):
        self.driver.quit()



# def print_OP_posts(posts):
#     for p in posts:
#         print(p)

# def print_COMMENTER_posts(posts):
#     for COMMENTER_pst in posts:
#         print(COMMENTER_pst)
