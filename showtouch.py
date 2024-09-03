import os
import time
from pynput import keyboard
from datetime import datetime, timedelta
import pyfiglet

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_key(key, key_history):
    clear_screen()
    
    if hasattr(key, 'char'):
        display_key = key.char
    elif hasattr(key, 'name'):
        display_key = key.name.upper()
    else:
        display_key = str(key)
    
    # Create ASCII art for the display key
    fig = pyfiglet.Figlet(font='big')
    ascii_art = fig.renderText(display_key)
    
    # Center each line of the ASCII art
    centered_ascii_art = '\n'.join(line.center(80) for line in ascii_art.split('\n'))
    
    print("\n" * 5)
    print(centered_ascii_art)
    print("\n" * 5)
    
    # Display last 3 lines of key history
    lines = []
    current_line = []
    for item, _ in key_history:
        if item == '•':
            if current_line:
                lines.append(' '.join(current_line))
                current_line = []
        else:
            current_line.append(item)
    if current_line:
        lines.append(' '.join(current_line))
    
    for line in lines[-3:]:
        print(line.center(80))
    
    return display_key

def on_press(key, key_history):
    current_time = datetime.now()
    display_key_str = display_key(key, key_history)
    
    if key_history:
        time_diff = current_time - key_history[-1][1]
        if time_diff > timedelta(seconds=1):
            key_history.append(("•", current_time))
    
    key_history.append((display_key_str, current_time))
    key_history = key_history[-60:]  # Keep a longer history for line breaks
    return key_history

def main():
    key_history = []
    
    print("ShowTouch CLI started. Press Esc to exit.")
    time.sleep(2)
    
    with keyboard.Listener(on_press=lambda key: on_press(key, key_history)) as listener:
        try:
            listener.join()
        except KeyboardInterrupt:
            print("\nExiting ShowTouch CLI...")

if __name__ == "__main__":
    main()