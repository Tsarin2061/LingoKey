import time
from pynput.keyboard import Key, KeyCode


class Keyboard:
    time_last_pressed = 0
    pressed_keys = set()

    def __init__(self, callback):
        self.callback = callback

    def on_press(self, key):
        shortcut_keys = [
            {Key.cmd, KeyCode.from_char("j")},
        ]
        try:
            self.pressed_keys.add(key)

            for shortcut in shortcut_keys:
                if all(k in self.pressed_keys for k in shortcut):
                    if time.time() - self.time_last_pressed < 1:
                        return None
                    self.time_last_pressed = time.time()
                    self.pressed_keys.remove(key)

                    self.callback()

            print('done')
        except AttributeError:
            pass

    def on_release(self, key):
        try:
            self.pressed_keys.remove(key)
        except KeyError:
            pass
