import os
import pygame
import tkinter as tk
from tkinter import messagebox, filedialog
import time
from PIL import Image, ImageTk
import tkinter.ttk as ttk

# Initialize pygame
pygame.init()

start_time = None
paused_time = 0

# Function to play music
def play_music(folder_path, selection_idx):
    try:
        audio_files = [file for file in os.listdir(folder_path) if file.endswith('.mp3') or file.endswith('.wav')]
        return audio_files
    except FileNotFoundError:
        messagebox.showerror("Error", "Invalid folder path")
        return None

# Function to pause music
def pause_music():
    global start_time, paused_time
    pygame.mixer.music.pause()
    if start_time:
        paused_time = time.time() - start_time
    start_time = None

# Function to resume music
def resume_music():
    global start_time
    pygame.mixer.music.unpause()
    if start_time is None:
        start_time = time.time() - paused_time

# Function to play the selected song
def play_song():
    global start_time
    start_time = time.time()
    folder_path = folder_entry.get()
    try:
        selection_idx = int(song_entry.get()) - 1
        audio_files = play_music(folder_path, selection_idx)
        if audio_files:
            selected_song = os.path.join(folder_path, audio_files[selection_idx])
            pygame.mixer.music.load(selected_song)
            pygame.mixer.music.play()
    except (ValueError, IndexError):
        messagebox.showerror("Error", "Invalid input for song number")

# Function to browse for a folder
def browse_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        folder_entry.delete(0, tk.END)
        folder_entry.insert(0, folder_selected)
        update_songs_list()

# Function to update the list of songs in the listbox
def update_songs_list():
    folder_path = folder_entry.get()
    audio_files = [file for file in os.listdir(folder_path) if file.endswith('.mp3') or file.endswith('.wav')]
    songs_listbox.delete(0, tk.END)
    for idx, song in enumerate(audio_files, start=1):
        songs_listbox.insert(tk.END, f"{idx}. {song}")

# Create a tkinter GUI
root = tk.Tk()
root.title("Music Player")

# Styling

# Load the GIF image
gif_image = Image.open("D:\cs\Keyfi\ErdoRadio\wallpaper.gif")
background_image = ImageTk.PhotoImage(gif_image)

# Set the background image
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

root.configure(bg='black')
root.geometry("400x350")

# Folder path input
folder_label = tk.Label(root, text="Enter Folder Path:", bg='#f0f0f0')
folder_label.pack()
folder_entry = tk.Entry(root, width=30)
folder_entry.pack()

# Browse button
browse_button = tk.Button(root, text="Browse", command=browse_folder, bg='#FFD700', fg='black')
browse_button.pack(pady=5)

# Song selection input
song_label = tk.Label(root, text="Enter Song Number:", bg='#f0f0f0')
song_label.pack()
song_entry = tk.Entry(root, width=30)
song_entry.pack()

# Add a listbox to display songs
songs_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=50)
songs_listbox.pack()

# Bind the update_songs_list function to folder entry
folder_entry.bind("<Return>", lambda event: update_songs_list())

# Play button
play_button = tk.Button(root, text="Play", command=play_song, bg='#4CAF50', fg='white')
play_button.pack(pady=5)

# Pause button
pause_button = tk.Button(root, text="Pause", command=pause_music, bg='#FF6347', fg='white')
pause_button.pack(pady=5)

# Resume button
resume_button = tk.Button(root, text="Resume", command=resume_music, bg='#1E90FF', fg='white')
resume_button.pack(pady=5)

# Create a label to display the timer
timer_label = tk.Label(root, text="00:00:00:000", bg='#f0f0f0')
timer_label.pack()

# Create a progress bar
progress_bar = ttk.Progressbar(root, length=200, mode='determinate')
progress_bar.pack()

def update_timer():
    if start_time:
        elapsed_time = time.time() - start_time
        hours, remainder = divmod(elapsed_time, 3600)
        minutes, seconds = divmod(remainder, 60)
        milliseconds = int((elapsed_time - int(elapsed_time)) * 1000)
        timer_label.config(text=f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}:{milliseconds:03d}")
        
        # Update the progress bar value based on elapsed time
        progress_bar['value'] = (elapsed_time % 60) / 60 * 100
        
    root.after(1, update_timer)

# Start the timer update loop
update_timer()

root.mainloop()
