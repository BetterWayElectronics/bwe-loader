import zlib
import base64
import tkinter as tk
from tkinter import filedialog
import pyperclip

def select_file():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(title="Select a MOD file", filetypes=(("MOD files", "*.mod *.xm"), ("All files", "*.*")))
    return file_path

def compress_and_encode(file_path):
    # Read the file
    with open(file_path, 'rb') as file:
        file_data = file.read()

    # Compress the data
    compressed_data = zlib.compress(file_data)

    # Encode the compressed data to base64
    encoded_data = base64.b64encode(compressed_data).decode('utf-8')

    return encoded_data

def save_to_clipboard(data):
    pyperclip.copy(data)
    print("Encoded data has been copied to the clipboard.")

if __name__ == "__main__":
    file_path = select_file()
    if file_path:
        encoded_data = compress_and_encode(file_path)
        save_to_clipboard(encoded_data)
    else:
        print("No file selected.")
