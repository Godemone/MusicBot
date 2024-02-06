import os
import pygame

# Initialize pygame
pygame.init()

# Function to play music
def play_music(folder_path):
    # List audio files in the folder
    audio_files = [file for file in os.listdir(folder_path) if file.endswith('.mp3') or file.endswith('.wav')]

    # Print available songs
    for idx, audio_file in enumerate(audio_files, start=1):
        print(f"{idx}. {audio_file}")

    # Get user selection
    selection_idx = int(input("Enter the number of the song you want to play: ")) - 1
    selected_song = os.path.join(folder_path, audio_files[selection_idx])

    # Load and play the selected song
    pygame.mixer.music.load(selected_song)
    pygame.mixer.music.play()

    # Control loop
    while True:
        control = input("Enter 'p' to pause, 'r' to resume, or 'q' to quit: ")
        if control == 'p':
            pygame.mixer.music.pause()
        elif control == 'r':
            pygame.mixer.music.unpause()
        elif control == 'q':
            pygame.mixer.music.stop()
            break

# Main program
if __name__ == "__main__":
    folder_path = input("Enter the folder path: ")
    play_music(folder_path)