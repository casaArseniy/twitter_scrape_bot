from datetime import datetime, timedelta
import sys
import time
from pynput import mouse
from pynput.mouse import Button, Controller

my_mouse = Controller()

def on_move(x, y):
    print('Pointer moved to {0}'.format(
        (x, y)))

def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    if not pressed:
        # Stop listener
        return False

def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))

listener = mouse.Listener(
    on_move=on_move,
    on_click=on_click,
    on_scroll=on_scroll)



def track_mouse(track_time):

    start = datetime.now()
    listener.start()
    while datetime.now() - start < timedelta(seconds=track_time):
        continue
    mouse.Listener.stop

def move_mouse():
    my_mouse.position = (10, 20)
    my_mouse.press(Button.right)




def main():

    #track_mouse(5)
    move_mouse()


if __name__ == "__main__":
    main()
