from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from soup import get_OP_soup, get_COMMENTER_soup
from table import *    

class Scrapper():

    def __init__(self):
        self.df_OP = create_Table()
        self.df_COMM = create_Table()
        self.df_REPLY = create_Table()
        self.name_tags = []
        self.driver = webdriver.Chrome()

    def go_to(self, html):
        self.driver.get(html)
    
    def clear_data(self):

        self.df_OP = create_Table()
        self.df_COMM = create_Table()
        self.df_REPLY = create_Table()

        self.name_tags = []

    
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
            html = self.driver.current_url
            time.sleep(1)
            with open("page.html", "w", encoding="utf-8") as f:
                f.write(html_content)
            
            psts = get_OP_soup()

            for pst in psts:
                self.df_OP = insert_post_into_Table(self.df_OP, html, pst)

            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)  # Wait for 2 seconds after each scroll
    
    def get_OP_name_tags(self):
        self.name_tags = set(self.df_OP['Name Tag'])
    
    def get_COMMENTER_posts(self, html):
        signal = 0
        index = 0
        self.driver.get(html)
        time.sleep(1)
        while (signal == 0 and index<2):  # Scroll down N times, adjust as needed
            html_content = self.driver.page_source
            with open("page.html", "w", encoding="utf-8") as f:
                f.write(html_content)
            psts, signal = get_COMMENTER_soup()

            for pst in psts:
                self.df_COMM = insert_post_into_Table(self.df_COMM, html, pst)     

            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)  # Wait for 2 seconds after each scroll
            index +=1
    
    def get_REPLY_tags(self, html):
        signal = 0
        index = 0
        name_tags = []

        self.driver.get(html)
        time.sleep(1)

        while (signal == 0 and index<2):  # Scroll down N times, adjust as needed
            html_content = self.driver.page_source
            with open("page.html", "w", encoding="utf-8") as f:
                f.write(html_content)
            tags, signal = get_COMMENTER_soup()   
            name_tags += tags
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)  # Wait for 2 seconds after each scroll
            index +=1
        
        return name_tags
    
    def access_OP_posts(self, scroll_number):
        self.get_OP_posts(scroll_number)
    
    def access_COMMENTER_posts(self):
        for index, row in self.df_OP.iterrows():
            self.get_COMMENTER_posts(row['Post URL'])
    
    def access_OP_REPLY_posts(self):
        self.get_OP_name_tags()
        for index, row in self.df_COMM.iterrows():
            if row['Num. of Replies'] > 0:
                print("HIT!!!")
                reply_name_tags = set(self.get_REPLY_tags(row['Post URL']))
                intersection = self.name_tags & reply_name_tags
                if len(intersection) == 0: # no reply from OP
                    self.df_COMM.at[index, 'Label'] = 0
                elif len(intersection) == 1: # reply from OP
                    self.df_COMM.at[index, 'Label'] = 1
                else:                   # convo with OP
                    self.df_COMM.at[index, 'Label'] = 2

    
    def save_data(self):
        table_to_csv(self.df_OP, 'OP')
        table_to_csv(self.df_COMM, 'COMMENTER')
    
    def close(self):
        self.driver.quit()
