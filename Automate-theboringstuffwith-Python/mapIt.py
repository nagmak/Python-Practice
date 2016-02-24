#! python3
# mapIt.py
# command line or clipboard

import webbrowser, sys
import pyperclip
address = ''
if len(sys.argv) > 1:
    # Get address from command line
    address = ' '.join(sys.argv[1:])

    #TODO: get address from clipboard
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.ca/maps/place/' + address)
