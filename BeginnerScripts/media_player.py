import tkinter as tk
from tkinter import filedialog
import pygame

# Initialiserer pygame mikseren
pygame.mixer.init()

# Initialiserer spilleliste
playlist = []
current_song_index = 0

# Funksjonen for å spille av lydfil
def play_music():
    if playlist:
        pygame.mixer.music.load(playlist[current_song_index])
        pygame.mixer.music.play()

# Funksjon for å pause musikken
def pause_music():
    pygame.mixer.music.pause()

# Funksjon for å gjenoppta musikken
def unpause_music():
    pygame.mixer.music.unpause()

# Funksjon for å stoppe avspillingen
def stop_music():
    pygame.mixer.music.stop()

# Funksjon for å legge til en ny fil til spillelisten
def add_to_playlist():
    files = filedialog.askopenfilenames(filetypes=[("Lydfiler", "*.mp3 *.wav")])
    playlist.extend(files)

# Funksjon for å spille neste sang i spillelisten
def next_song():
    global current_song_index
    if playlist:
        current_song_index = (current_song_index + 1) % len(playlist)
        play_music()

# Funksjon for å spille forrige sang i spillelisten
def prev_song():
    global current_song_index
    if playlist:
        current_song_index = (current_song_index - 1) % len(playlist)
        play_music()

# Setter opp hovedvinduet
root = tk.Tk()
root.title("Utvidet Mediaspiller")

# Knapp for å legge til musikk i spillelisten
add_button = tk.Button(root, text="Legg til Musikk", command=add_to_playlist)
add_button.pack(pady=5)

# Knapp for å spille av musikk
play_button = tk.Button(root, text="Spill Musikk", command=play_music)
play_button.pack(pady=5)

# Knapp for å pause musikken
pause_button = tk.Button(root, text="Pause", command=pause_music)
pause_button.pack(pady=5)

# Knapp for å gjenoppta musikken
unpause_button = tk.Button(root, text="Gjenoppta", command=unpause_music)
unpause_button.pack(pady=5)

# Knapp for å stoppe musikken
stop_button = tk.Button(root, text="Stopp", command=stop_music)
stop_button.pack(pady=5)

# Knapp for å spille neste sang
next_button = tk.Button(root, text="Neste", command=next_song)
next_button.pack(pady=5)

# Knapp for å spille forrige sang
prev_button = tk.Button(root, text="Forrige", command=prev_song)
prev_button.pack(pady=5)

# Kjører hovedløkken
root.mainloop()