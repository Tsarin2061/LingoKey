from pynput.keyboard import Key, Controller
import pyperclip
import Quartz
from AppKit import NSPasteboard, NSPasteboardTypeString
import time

def simulate_ctrl_c():
    keyboard = Controller()

    # Press Command key
    keyboard.press(Key.cmd)
    time.sleep(0.1)  # Small delay to ensure the keypress is registered

    # Press 'c' key
    keyboard.press('c')

    # Release 'c' key
    keyboard.release('c')

    # Release Command key
    keyboard.release(Key.cmd)

    print(get_clipboard())


def get_clipboard():
    # Get the text from the clipboard
    clipboard_text = pyperclip.paste()
    return clipboard_text

def past_into_clipboard(text):
    pyperclip.copy(text)

def paste_text():
    # Convert clipboard content to an event
    paste_event = Quartz.CGEventCreateKeyboardEvent(None, 9, True)
    Quartz.CGEventSetFlags(paste_event, Quartz.kCGEventFlagMaskCommand)
    Quartz.CGEventPost(Quartz.kCGAnnotatedSessionEventTap, paste_event)
