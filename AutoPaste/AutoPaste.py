import keyboard
import win32clipboard
from pyKey import pressKey, releaseKey, press, sendSequence, showKeys


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
            if K == "~":
                K = "TILDE"
            if K == " ":
                K = "SPACEBAR"
            print(K)
            press(str(K))
        break
    else:
        print(keyboard.read_key())