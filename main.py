from gui import *
from credentials import ID, PASSWORD

login(ID, PASSWORD)
time.sleep(3)
driver.get("https://twitter.com/Microsoft")
create_GUI()