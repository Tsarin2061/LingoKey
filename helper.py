import platform
import logging
import time
import pyperclip


def get_clipboard():
    clipboard_text = pyperclip.paste()
    logging.debug(f"Text from clipboard: {clipboard_text}")
    return clipboard_text

def past_into_clipboard(text):
    logging.debug(f"Text to clipboard: {text}")
    pyperclip.copy(text)


