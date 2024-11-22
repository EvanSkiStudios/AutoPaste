import keyboard
import win32clipboard
from pyKey import pressKey, releaseKey, press, sendSequence, showKeys
# https://github.com/gauthsvenkat/pyKey/blob/master/pyKey/key_dict.py


while True:  # making a loop
    print("Waiting...")
    if keyboard.read_key() == "f2":
        # print("Key pressed")
        # get clipboard data
        win32clipboard.OpenClipboard()
        clipboardData = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()

        # loop through string and press the keys
        for K in clipboardData:
            print(repr(K))

            if K == "~":
                K = "TILDE"
            elif K == " ":
                K = "SPACEBAR"
            elif (K == "\r") or (K == "\n"):
                K = "ENTER"
            elif K == "\t":
                K = "TAB"

            press(str(K))
        break
    else:
        print(keyboard.read_key())
