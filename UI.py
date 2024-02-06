import os
import pygame
import tkinter as tk
from tkinter import messagebox

# Initialize pygame
pygame.init()

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
    pygame.mixer.music.pause()

# Function to resume music
def resume_music():
    pygame.mixer.music.unpause()

# Create a tkinter GUI
root = tk.Tk()
root.title("Music Player")

# Styling
root.configure(bg='black')
root.geometry("400x300")

# Folder path input
folder_label = tk.Label(root, text="Enter Folder Path:", bg='#f0f0f0')
folder_label.pack()
folder_entry = tk.Entry(root, width=30)
folder_entry.pack()

# Song selection input
song_label = tk.Label(root, text="Enter Song Number:", bg='#f0f0f0')
song_label.pack()
song_entry = tk.Entry(root, width=30)
song_entry.pack()

# Add a listbox to display songs
songs_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=50)
songs_listbox.pack()

# Function to update the songs list when folder path is entered
def update_songs_list():
    folder_path = folder_entry.get()
    audio_files = play_music(folder_path, 0)  # Get the list of songs
    if audio_files:
        songs_listbox.delete(0, tk.END)  # Clear existing list
        for idx, song in enumerate(audio_files, start=1):
            songs_listbox.insert(tk.END, f"{idx}. {song}")

# Bind the update_songs_list function to folder entry
folder_entry.bind("<Return>", lambda event: update_songs_list())

# Play button
def play_song():
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

play_button = tk.Button(root, text="Play", command=play_song, bg='#4CAF50', fg='white')
play_button.pack(pady=5)

# Pause button
pause_button = tk.Button(root, text="Pause", command=pause_music, bg='#FF6347', fg='white')
pause_button.pack(pady=5)

# Resume button
resume_button = tk.Button(root, text="Resume", command=resume_music, bg='#1E90FF', fg='white')
resume_button.pack(pady=5)

root.mainloop()