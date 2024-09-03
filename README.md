# ShowTouch 1.0

ASCII Keypress Visualizer


https://github.com/user-attachments/assets/fbe8c2de-3b9a-449d-b3d8-fa0556c34f96


## DESCRIPTION
     ShowTouch is a CLI utility that displays keypresses in real-time
     using ASCII art. It provides a visually striking representation
     of keyboard input, useful for presentations, screencasts, or
     just for fun.

## SYNOPSIS
     python showtouch.py

## REQUIREMENTS
     - Python 3.x
     - pynput
     - pyfiglet

## INSTALLATION
     1. Ensure Python 3.x is installed on your system.
     2. Install required libraries:
        $ pip install pynput pyfiglet

USAGE
     Run the script from the command line:
     $ python showtouch.py

     Press keys to see them displayed in ASCII art.
     A history of recent keypresses is shown at the bottom.
     Pauses longer than 1 second are indicated by dots.

     To exit, press Ctrl+C.

## FEATURES
     - Large ASCII art display of current keypress
     - Rolling 3-line history of recent keypresses
     - Visual indication of typing pauses

## KNOWN ISSUES
     - May not capture all system-level hotkeys
     - Performance may degrade on very old systems

## ACKNOWLEDGEMENTS
     Thanks to the creators of pynput and pyfiglet.
