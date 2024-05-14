import time
from pynput import keyboard
from pynput.keyboard import Key, KeyCode

class Keyboard():

    time_last_pressed = 0
    pressed_keys = set()

    def __init__(self, callback):
        self.callback = callback
        pass

    def on_press(self,key):
        shortcut_keys = [
            {Key.ctrl_l, Key.alt_l}
        ]
        try:
            self.pressed_keys.add(key)
        
            for shortcut in shortcut_keys:
                if all(k in self.pressed_keys for k in shortcut):
                    if time.time() - self.time_last_pressed < 1: return None
                    self.time_last_pressed = time.time() 
                    self.callback()
        except AttributeError:
            pass

    def on_release(self,key):
        try:
            self.pressed_keys.remove(key)
        except KeyError:
            pass  

