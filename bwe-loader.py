
import zlib
import base64
import sys
import io
import os
from contextlib import redirect_stdout
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import threading
import random

# Base64 encoded zlib compressed .mod file 
#1 CLASS06
#2 KAP
#3 ORIGIN1
#4 RAZOR02
#5 SAC08

encoded_songs = [
    "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",  # Replace these with your actual base64 encoded song data
    "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",
]

current_song_index = 0

def decode_mod_data(encoded_data):
    # Decode from base64
    compressed_data = base64.b64decode(encoded_data)

    # Decompress the data
    mod_data = zlib.decompress(compressed_data)

    return mod_data

def play_mod_data(mod_data):
    with open(os.devnull, 'w') as f, redirect_stdout(f):
        pygame.mixer.init()
        pygame.display.set_caption("")

    # Use BytesIO to play the data in memory
    mod_file = io.BytesIO(mod_data)
    pygame.mixer.music.load(mod_file)
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)  # Loop the music indefinitely

    # Keep the script running until the music finishes playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

def play_next_song():
    global current_song_index
    song_data = encoded_songs[current_song_index]
    mod_data = decode_mod_data(song_data.strip())
    music_thread = threading.Thread(target=play_mod_data, args=(mod_data,))
    music_thread.daemon = True
    music_thread.start()
    current_song_index = (current_song_index + 1) % len(encoded_songs)

def print_banner() -> str:
    sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=32, cols=130))
    banner = r"""
__________         ___________.____                     .___            
\______   \__  _  _\_   _____/|    |    _________     __| _/___________ 
 |    |  _/\ \/ \/ /|    __)_ |    |   /  _ \__  \   / __ |/ __ \_  __ \
 |    |   \ \     / |        \|    |__(  <_> ) __ \_/ /_/ \  ___/|  | \/
 |______  /  \/\_/ /_______  /|_______ \____(____  /\____ |\___  >__|   
        \/                 \/         \/         \/      \/    \/       
"""
    os.system("")
    faded_banner = ""
    colors = [
        (85, 0, 145),   # Dark purple
        (99, 43, 153),  # Intermediate colour 1
        (122, 87, 176), # Intermediate colour 2
        (146, 130, 199),# Intermediate colour 3
        (169, 173, 222),# Intermediate colour 4
        (173, 216, 230),# Intermediate colour 5
        (173, 216, 230) # Light blue
    ]   
    color_index = 0

    for line in banner.splitlines():
        r, g, b = colors[color_index]
        faded_banner += (f"\033[38;2;{r};{g};{b}m{line}\033[0m\n")
        color_index = (color_index + 1) % len(colors)
    return faded_banner

def fade(text: str) -> str:
    os.system("")
    faded = ""
    green = 194
    for line in text:
        faded += (f"\033[38;2;0;{green};199m{line}\033[0m")
        if green != 0:
            green -= 6
            if green < 0:
                green = 0
    return faded

def gradient_text(text: str, colors: list) -> str:
    os.system("")
    gradient = ""
    color_index = 0
    for char in text:
        if char != " ":
            r, g, b = colors[color_index]
            gradient += f"\033[38;2;{r};{g};{b}m{char}\033[0m"
            color_index = (color_index + 1) % len(colors)
        else:
            gradient += char
    return gradient

def print_menu():
    colors = [
        (169, 173, 222),# Intermediate colour 4
        (173, 216, 230),# Intermediate colour 5
        (173, 216, 230) # Light blue
    ]
    menu_items = [
        "Select Which BwE App You Want To Run:\n",
        "1. BwE PS4 NOR Validator + Syscon Patcher",
        "2. BwE PS4 Syscon Rebuilder",
        "3. BwE PS4 UART Syscon Tools",
        "-------------------------------",
        "4. BwE PS5 NOR Tools",
        "5. BwE PS5 Code Reader",
        "6. BwE PS5 Southbridge Console",
        "-------------------------------",
        "M. Turn Off Music",
        "N. Play Next Song",
        "Q. Quit",
        "\nMake Your Selection: "
    ]
    for item in menu_items[:-1]:
        print(gradient_text(item, colors))
    print(gradient_text(menu_items[-1], colors), end='')

def main():
    # Start playing the first song
    play_next_song()
    
    while True:
        os.system("cls")
        print(print_banner())
        print_menu()
        selection = input().strip().upper()
        if selection == 'M':
            pygame.mixer.music.stop()
            
        elif selection == 'N':
            pygame.mixer.music.stop()
            play_next_song()
            
        elif selection == 'Q':
            exit()
        else:
            main()

if __name__ == "__main__":
    main()
