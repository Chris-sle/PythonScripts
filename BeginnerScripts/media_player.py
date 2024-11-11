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
after_id = None

def play_music(start_position=None):
    """Play music from a specified starting position."""
    if not playlist:
        return

    track = playlist[current_song_index]
    pygame.mixer.music.load(track)

    if start_position is not None:
        pygame.mixer.music.play(loops=0, start=start_position)
    else:
        pygame.mixer.music.play(loops=0)

    # Update song information
    update_song_info(track)
    # Ensure progress updates are continuously checked
    start_checking_progress()

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
    """Stop the music and reset the playback position and state."""
    pygame.mixer.music.stop()
    global paused_position, is_paused, after_id
    paused_position = 0
    is_paused = False
    if after_id is not None:
        root.after_cancel(after_id)
        after_id = None
    progress_scale.set(0)  # Reset progress bar to beginning

def add_to_playlist():
    """Add songs to the playlist."""
    files = filedialog.askopenfilenames(filetypes=[("Lydfiler", "*.mp3 *.wav")])
    playlist.extend(files)
    if playlist:
        play_music()

def next_song():
    """Skip to the next song in the playlist."""
    global current_song_index, paused_position
    paused_position = 0
    if not playlist:
        return
    current_song_index = (current_song_index + 1) % len(playlist)
    play_music()

def prev_song():
    """Return to the previous song in the playlist."""
    global current_song_index, paused_position
    paused_position = 0
    if playlist:
        current_song_index = (current_song_index - 1) % len(playlist)
        play_music()

def start_checking_progress():
    """Start or continue checking the playback progress."""
    global after_id
    if after_id is not None:
        root.after_cancel(after_id)  # Cancel any existing scheduled checks
    after_id = root.after(1000, check_music)

def check_music():
    """Continuously update the song's playback progress and switch when a song ends."""
    update_progress()
    if not pygame.mixer.music.get_busy() and playlist and not is_paused:
        next_song()
    
def update_progress():
    """Update the progress scale with the current playback position."""
    if pygame.mixer.music.get_busy():
        position = pygame.mixer.music.get_pos() // 1000
        progress_scale.set(position)

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
    pos = int(float(val))
    if pygame.mixer.music.get_busy():  # Only set position if music is currently playing
        pygame.mixer.music.set_pos(pos)  # This sets the position without restarting playback
    else:
        play_music(start_position=pos)  # If stopped, play from the selected position
        
def suppress_auto_update():
    """Allow the progress bar to update only when manipulated by the user."""
    progress_scale.bind("<ButtonRelease-1>", lambda event: set_position(progress_scale.get()))
    progress_scale.bind("<Motion>", lambda event: None)

def set_volume(val):
    """Adjust the playback volume."""
    volume = float(val) / 100
    pygame.mixer.music.set_volume(volume)

# Create the main application window
root = tk.Tk()
root.title("Utvidet Mediaspiller")

song_info = tk.StringVar()

# Create the song information label
song_info_label = tk.Label(root, textvariable=song_info, width=50)
song_info_label.pack(pady=5)

# Create the progress scale
progress_scale = tk.Scale(root, orient='horizontal', command=set_position, showvalue=0, length=400)
progress_scale.pack(pady=5)

# Create buttons for controlling the music
add_button = tk.Button(root, text="Add Music", command=add_to_playlist)
add_button.pack(pady=1)

play_button = tk.Button(root, text="Play Music", command=play_music)
play_button.pack(pady=5)

pause_button = tk.Button(root, text="Pause", command=pause_music)
pause_button.pack(pady=5)

unpause_button = tk.Button(root, text="Unpause", command=unpause_music)
unpause_button.pack(pady=5)

stop_button = tk.Button(root, text="Stop", command=stop_music)
stop_button.pack(pady=5)

next_button = tk.Button(root, text="Next", command=next_song)
next_button.pack(pady=5)

prev_button = tk.Button(root, text="Previous", command=prev_song)
prev_button.pack(pady=5)

# Create the volume scale
volume_scale = tk.Scale(root, from_=0, to=100, orient='horizontal', command=set_volume, label="Volum")
volume_scale.set(50)  # Set default volume to 50%
volume_scale.pack(pady=5)

# Call the method to suppress automatic updates
suppress_auto_update()

# Start checking the music status
root.after(1000, check_music)

# Run the application
root.mainloop()