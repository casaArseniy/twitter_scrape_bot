import tkinter as tk
from selenium import webdriver
import time
from soup import get_OP_soup, get_COMMENTER_soup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from table import *

N = 1
driver = webdriver.Chrome()

OP_POSTS = []
COMMENTER_POSTS = []

df_OP = create_Table()
df_COMM = create_Table()

def login(ID, PASSWORD):
    driver.get("https://twitter.com/i/flow/login")
    time.sleep(3)
    # Find the input element by class name
    input_element = driver.find_element(By.CLASS_NAME, 'r-30o5oe')
    # Input text into the element
    input_element.send_keys(ID)
    input_element.send_keys(Keys.ENTER)
    time.sleep(3)
    input_element = driver.find_element(By.NAME, 'password')
    input_element.send_keys(PASSWORD)
    input_element.send_keys(Keys.ENTER)

def print_OP_posts(posts):
    for p in posts:
        print(p)

def print_COMMENTER_posts(posts):
    for COMMENTER_pst in posts:
        print(COMMENTER_pst)

def get_OP_posts():

    global N
    posts = []

    for i in range(N):  # Scroll down N times, adjust as needed
        html_content = driver.page_source
        time.sleep(1)
        with open("page.html", "w", encoding="utf-8") as f:
            f.write(html_content)
        posts+=get_OP_soup()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # Wait for 2 seconds after each scroll
    
    html = driver.current_url
    return posts, html

def get_COMMENTER_posts(OP_pst):
    posts = []
    signal = 0
    index = 0
    html = OP_pst.url

    driver.get(html)
    time.sleep(1)

    while (signal == 0 and signal<2):  # Scroll down N times, adjust as needed
        html_content = driver.page_source
        with open("page.html", "w", encoding="utf-8") as f:
            f.write(html_content)
        pst, signal = get_COMMENTER_soup()
        posts+=pst
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # Wait for 2 seconds after each scroll
        index +=1

    return posts, html

def access_OP_posts():
    global OP_POSTS
    global df_OP
    OP_POSTS, html = get_OP_posts()
    # do something with them
    for pst in OP_POSTS:
        df_OP = insert_post_into_Table(df_OP, html, pst)
    #print_OP_posts(OP_POSTS)

def access_COMMENTER_posts():
    global COMMENTER_POSTS
    global OP_POSTS
    global df_COMM

    for post in OP_POSTS:
        cmt_pst, html = get_COMMENTER_posts(post)
        for pst in cmt_pst:
            df_COMM = insert_post_into_Table(df_COMM, html, pst)

        COMMENTER_POSTS.append(cmt_pst)
    # do something with them
    # for posts in COMMENTER_POSTS:
    #     print_COMMENTER_posts(posts)

def table_to_csv():
    global df_OP
    global df_COMM

    df_OP.to_csv('twitter_scrape_bot/data/OP_Posts.csv', index=False)
    df_COMM.to_csv('twitter_scrape_bot/data/OP_Comment_Posts.csv', index=False)


def create_GUI():
    # Create the main window
    root = tk.Tk()
    root.title("GUI Button Example")

    def on_closing():
        driver.quit()
        root.destroy()  # Close the GUI window

    root.protocol("WM_DELETE_WINDOW", on_closing)

    # Function to be executed when the button is clicked
    button_function_OP = lambda: access_OP_posts() # OP posts
    button_function_COMMENTER = lambda: access_COMMENTER_posts() # COMMENTER posts
    button_function_EXTRACT = lambda: table_to_csv()

    # Create a button widget
    button_OP = tk.Button(root, text="OP Posts", command=button_function_OP)
    button_OP.pack(pady=20)

    button_COMMENTER = tk.Button(root, text="Commenter Posts", command=button_function_COMMENTER)
    button_COMMENTER.pack(pady=20)

    button_EXTRACT = tk.Button(root, text="Extract Data", command=button_function_EXTRACT)
    button_EXTRACT.pack(pady=20)

    # Run the event loop
    root.mainloop()