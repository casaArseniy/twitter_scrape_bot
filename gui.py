import tkinter as tk
from selenium import webdriver
import time
from soup import get_OP_soup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from credentials import ID, PASSWORD 

N = 1
driver = webdriver.Chrome()

OP_POSTS = []
COMMENTER_POSTS = []

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

def print_posts(posts):
    for p in posts:
        print(p)

def grab_posts(scrolls_num):
    posts = []
    for i in range(scrolls_num):  # Scroll down 5 times, adjust as needed
        html_content = driver.page_source
        with open("page.html", "w", encoding="utf-8") as f:
            f.write(html_content)
        time.sleep(1)
        posts+=get_OP_soup()
        # print_posts(posts)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # Wait for 2 seconds after each scroll
    return posts

def access_posts(type):
    global OP_POSTS
    global COMMENTER_POSTS
    global N

    if type == 0: # OP
        OP_POSTS = grab_posts(N)
        print_posts(OP_POSTS)
    else:
        get_commenter_posts()
        print_posts(COMMENTER_POSTS)

def get_commenter_posts():
    global OP_POSTS
    global COMMENTER_POSTS

    for post in OP_POSTS:
        if post.num_replies >=2:
            driver.get(post.url)
            time.sleep(3)
            COMMENTER_POSTS.append(grab_posts(3))


def create_GUI():
    # Create the main window
    root = tk.Tk()
    root.title("GUI Button Example")

    def on_closing():
        driver.quit()
        root.destroy()  # Close the GUI window

    root.protocol("WM_DELETE_WINDOW", on_closing)

    # Function to be executed when the button is clicked
    button_function_OP = lambda: access_posts(0) # OP posts
    button_function_COMMENTER = lambda: access_posts(1) # COMMENTER posts

    # Create a button widget
    button_OP = tk.Button(root, text="OP POSTS", command=button_function_OP)
    button_OP.pack(pady=20)

    # button_OP = tk.Button(root, text="OP POSTS", command=button_function_OP)
    # button_OP.pack(pady=20)

    button_COMMENTER = tk.Button(root, text="COMMENTER POSTS", command=button_function_COMMENTER)
    button_COMMENTER.pack(pady=20)

    # Run the event loop
    root.mainloop()

login(ID, PASSWORD)
time.sleep(3)
driver.get("https://twitter.com/Microsoft")
create_GUI()