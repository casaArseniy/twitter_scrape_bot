from gui import create_GUI
from credentials import ID, PASSWORD
import time

from scrapper_classes.scrapper import Scrapper

s = Scrapper()

s.login(ID, PASSWORD)

time.sleep(5)

create_GUI(s)