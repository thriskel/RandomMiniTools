# -*- coding: utf-8 -*-
# Author: Manuel Martinez aka thriskel
# Description: Emulate a key press inside a window

import win32gui
import win32con
import time

# Simulate pressing a key
def send_key_press(window_title, key_code):
    # Find the target window by its title
    while True:
        window = win32gui.FindWindow(None, window_title)
        if window != 0:
            break

    while True:
        # Simulate a key press inside the target window in a simple manner
        # Send the key press to the target window using SendMessage
        win32gui.SendMessage(window, win32con.WM_KEYDOWN, key_code, 0)
        time.sleep(0.1)  # Sleep for a short duration to simulate key press
        win32gui.SendMessage(window, win32con.WM_KEYUP, key_code, 0)

        # Sleep for a bit so we don't eat up all the CPU
        time.sleep(0.5)


if __name__ == '__main__':
    key_to_press = ord('3')
    send_key_press('World of Warcraft', key_to_press)