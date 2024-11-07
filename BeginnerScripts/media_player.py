import tkinter as tk
from tkinter import filedialog
import pygame
from mutagen import File

pygame.mixer.init()

playlist = []
current_song_index = 0
current_song_length = 0
paused_position = 0
is_paused = False  # Track the pause state

def play_music(start_position=0):
    """Play music from a specified starting position."""
    if playlist:
        track = playlist[current_song_index]
        pygame.mixer.music.load(track)
        pygame.mixer.music.play(loops=0, start=start_position)  # Play from the specified position
        
        # Update song information
        update_song_info(track)

def update_song_info(file_path):
    """Update the song information and track length for the GUI."""
    global current_song_length
    try:
        audio = File(file_path)
        if audio:
            song_title = audio.get("TIT2", "Ukjent tittel")
            artist = audio.get("TPE1", "Ukjent artist")
            current_song_length = int(audio.info.length)
            song_info.set(f"Tittel: {song_title}, Artist: {artist}, Lengde: {current_song_length // 60}:{current_song_length % 60:02}")
            progress_scale.config(to=current_song_length)
        else:
            song_info.set("Kunne ikke hente informasjon om sangen.")
    except Exception as e:
        song_info.set(f"Feil ved henting av data: {e}")

def pause_music():
    """Pause the music and save the current position."""
    global paused_position, is_paused
    if not is_paused:  # Only pause if not already paused
        paused_position = pygame.mixer.music.get_pos() // 1000  # Save the position in seconds
        pygame.mixer.music.pause()
        is_paused = True

def unpause_music():
    """Resume the music from the last paused position."""
    global is_paused
    if is_paused:
        pygame.mixer.music.unpause()
        is_paused = False

def stop_music():
    """Stop the music and reset the position tracker."""
    pygame.mixer.music.stop()
    global paused_position, is_paused
    paused_position = 0
    is_paused = False  # Reset pause state

def add_to_playlist():
    """Add songs to the playlist."""
    files = filedialog.askopenfilenames(filetypes=[("Lydfiler", "*.mp3 *.wav")])
    playlist.extend(files)
    if playlist:
        play_music()  # Autoplay first song in the playlist

def next_song():
    """Skip to the next song in the playlist."""
    global current_song_index, paused_position
    paused_position = 0  # Reset paused position for the next song
    if playlist:
        current_song_index = (current_song_index + 1) % len(playlist)
        play_music()

def prev_song():
    """Return to the previous song in the playlist."""
    global current_song_index, paused_position
    paused_position = 0  # Reset paused position for the previous song
    if playlist:
        current_song_index = (current_song_index - 1) % len(playlist)
        play_music()

def check_music():
    """Continuously update the song's playback progress and switch when a song ends."""
    update_progress()
    if not pygame.mixer.music.get_busy() and playlist:
        next_song()  # Automatically play the next song if the current one ends
    root.after(1000, check_music)  # Update every second

def play_song_from(time):
    """Play the current song from a specific time."""
    play_music(start_position=time)

def update_progress():
    """Update the progress scale with the current playback position."""
    if pygame.mixer.music.get_busy():
        position = pygame.mixer.music.get_pos() // 1000
        progress_scale.set(position)

def set_position(val):
    """Set the song position to a new time when the progress scale is used."""
    pos = int(float(val))  # Get the new position in seconds
    play_song_from(pos)  # Call the play_song_from function to play from the new position

def set_volume(val):
    """Adjust the playback volume."""
    volume = float(val) / 100
    pygame.mixer.music.set_volume(volume)

root = tk.Tk()
root.title("Utvidet Mediaspiller")

song_info = tk.StringVar()

song_info_label = tk.Label(root, textvariable=song_info, width=50)
song_info_label.pack(pady=5)

progress_scale = tk.Scale(root, orient='horizontal', command=set_position, showvalue=0, length=400)
progress_scale.pack(pady=5)

add_button = tk.Button(root, text="Legg til Musikk", command=add_to_playlist)
add_button.pack(pady=1)

play_button = tk.Button(root, text="Spill Musikk", command=play_music)
play_button.pack(pady=5)

pause_button = tk.Button(root, text="Pause", command=pause_music)
pause_button.pack(pady=5)

unpause_button = tk.Button(root, text="Gjenoppta", command=unpause_music)
unpause_button.pack(pady=5)

stop_button = tk.Button(root, text="Stopp", command=stop_music)
stop_button.pack(pady=5)

next_button = tk.Button(root, text="Neste", command=next_song)
next_button.pack(pady=5)

prev_button = tk.Button(root, text="Forrige", command=prev_song)
prev_button.pack(pady=5)

volume_scale = tk.Scale(root, from_=0, to=100, orient='horizontal', command=set_volume, label="Volum")
volume_scale.set(50)
volume_scale.pack(pady=5)

# Start checking music and updating progress
root.after(1000, check_music)

# Start the Tkinter main loop
root.mainloop()