from pynput.keyboard import Key, Controller
import pyperclip
import Quartz
from AppKit import NSPasteboard, NSPasteboardTypeString


def simulate_ctrl_c():
    keyboard = Controller()

    keyboard.press(Key.ctrl)
    keyboard.press("c")

    keyboard.release("c")
    keyboard.release(Key.ctrl)


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
