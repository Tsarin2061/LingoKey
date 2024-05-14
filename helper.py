from pynput.keyboard import Key, Controller
import pyperclip
import keyboard
import pyautogui
import time


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

def paste_text():
    try:
        # Use pyautogui to simulate pressing Ctrl+V to paste
        pyautogui.hotkey('ctrl', 'v')
        # Add a short delay to allow time for the paste operation
        time.sleep(0.5)
    except Exception as e:
        print("Error:", e)
