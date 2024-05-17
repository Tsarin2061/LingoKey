import time
import pyperclip

def get_clipboard():
    # Get the text from the clipboard
    clipboard_text = pyperclip.paste()
    return clipboard_text

def past_into_clipboard(text):
    # Set the text into the clipboard: text
    pyperclip.copy(text)
