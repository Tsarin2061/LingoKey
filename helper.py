from pynput.keyboard import Key, Controller
import pyperclip


def simulate_ctrl_c():
    keyboard = Controller()
    keyboard.press(Key.ctrl.value)
    keyboard.press('c')
    keyboard.release('c')
    keyboard.release(Key.ctrl.value)

def get_clipboard():
    # Get the text from the clipboard
    clipboard_text = pyperclip.paste()
    return clipboard_text

def past_into_clipboard(text):
    pyperclip.copy(text)

def paste_text(text):
    keyboard = Controller()
    keyboard.type(text)
    print(text)
    