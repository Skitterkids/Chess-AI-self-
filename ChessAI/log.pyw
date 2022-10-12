from pynput.mouse import Listener
import logging

logging.basicConfig(filename="mouse_log.txt", level=logging.DEBUG, format="%(asctime)s: %(message)s")

def on_move(x, y):
    logging.info("Moved to ({0}, {1}))".format(x, y))
    pass

def on_click(x, y, button, pressed):
    logging.info("Clicked at ({0}, {1}) with {2})".format(x, y, button))
    pass

def on_scroll(x, y, dx, dy):
    logging.info("Scrolled at ({0}, {1})({2}, {3}))".format(x, y, dx, dy))
    pass

with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
    listener.join()