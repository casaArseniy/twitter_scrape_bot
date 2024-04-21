import tkinter as tk
from selenium import webdriver
import time
from soup import get_soup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from credentials import ID, PASSWORD 

N = 5
driver = webdriver.Chrome()

OP_posts = []
reply_posts = []

current_OP_post = ""
saved_repy = ""

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

def grab_OP_posts(N):
    for i in range(N):  # Scroll down 5 times, adjust as needed
        html_content = driver.page_source
        with open("page.html", "w", encoding="utf-8") as f:
            f.write(html_content)
        time.sleep(1)
        posts = get_soup()
        print_posts(posts)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # Wait for 2 seconds after each scroll
    


def create_GUI(N):
    # Create the main window
    root = tk.Tk()
    root.title("GUI Button Example")

    def on_closing():
        driver.quit()
        root.destroy()  # Close the GUI window

    root.protocol("WM_DELETE_WINDOW", on_closing)

    # Function to be executed when the button is clicked
    button_function = lambda: grab_OP_posts(N)

    # Create a button widget
    button = tk.Button(root, text="Click Me", command=button_function)
    button.pack(pady=20)

    # Run the event loop
    root.mainloop()

login(ID, PASSWORD)

time.sleep(3)
driver.get("https://twitter.com/Microsoft")

create_GUI(N)