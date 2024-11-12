import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk, ImageOps
import pygame
import os

# Global variables
total_duration = 0
repeat_mode = False
pygame_initialized = False

# Create main window
root = tk.Tk()
root.title("Music Player")
root.geometry("800x400")
root.config(bg="#1C1C1E")

# Function to initialize pygame mixer (lazy initialization)
def initialize_pygame():
    global pygame_initialized
    if not pygame_initialized:
        pygame.mixer.init()
        pygame_initialized = True

# Function to load a music file
def load_music():
    initialize_pygame()
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav")])
    if file_path:
        pygame.mixer.music.load(file_path)
        song_title.set(os.path.basename(file_path))
        play_button.config(state=tk.NORMAL)
        stop_button.config(state=tk.NORMAL)
        pause_button.config(state=tk.NORMAL)
        resume_button.config(state=tk.NORMAL)
        repeat_button.config(state=tk.NORMAL)
        update_music_length(file_path)

# Function to play the loaded music
def play_music():
    pygame.mixer.music.play()
    update_progress_bar()

# Function to stop the music
def stop_music():
    pygame.mixer.music.stop()
    progress['value'] = 0
    current_time_label.config(text="00:00")

# Function to pause the music
def pause_music():
    pygame.mixer.music.pause()

# Function to resume the music
def resume_music():
    pygame.mixer.music.unpause()

# Toggle repeat mode
def toggle_repeat():
    global repeat_mode
    repeat_mode = not repeat_mode
    repeat_button.config(relief=tk.SUNKEN if repeat_mode else tk.RAISED)

# Play the song again if repeat mode is on and song has ended
def check_repeat():
    if repeat_mode and not pygame.mixer.music.get_busy():
        play_music()

# Update total length and display it
def update_music_length(file_path):
    global total_duration
    sound = pygame.mixer.Sound(file_path)
    total_duration = sound.get_length()
    total_time_label.config(text=format_time(int(total_duration)))

# Format time in mm:ss
def format_time(seconds):
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{minutes:02}:{seconds:02}"

# Update the progress bar and time labels
def update_progress_bar():
    if pygame.mixer.music.get_busy():
        current_position = pygame.mixer.music.get_pos() / 1000
        progress['value'] = (current_position / total_duration) * 100
        current_time_label.config(text=format_time(int(current_position)))
        
        root.after(1000, update_progress_bar)
    else:
        if progress['value'] >= 100:
            progress['value'] = 0
            current_time_label.config(text="00:00")
        check_repeat()

# Load button images with error handling
def load_image(image_path):
    try:
        img = Image.open(image_path).resize((50, 50))
        img = ImageOps.expand(img, border=10, fill="#282828")
        img = ImageOps.fit(img, (50, 50), method=0, bleed=0.1, centering=(0.5, 0.5))
        return ImageTk.PhotoImage(img)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load image {image_path}: {e}")
        return None

# Load button images after root window is created
load_photo = load_image("icons/load.png")
play_photo = load_image("icons/play.png")
pause_photo = load_image("icons/pause.png")
resume_photo = load_image("icons/resume.png")
stop_photo = load_image("icons/stop.png")
repeat_photo = load_image("icons/repeat.png")

# Song title variable
song_title = tk.StringVar()
song_title.set("No song loaded")

# Frame for placing title and song info in the top center
title_frame = tk.Frame(root, bg="#1C1C1E")
title_frame.pack(pady=10)

title_label = tk.Label(title_frame, text="Music Player", font=("Arial", 18, "bold"), bg="#1C1C1E", fg="white")
title_label.pack()

song_label = tk.Label(title_frame, textvariable=song_title, font=("Arial", 14), bg="#1C1C1E", fg="white")
song_label.pack()

# Frame for buttons at the center
button_frame = tk.Frame(root, bg="#1C1C1E")
button_frame.pack(pady=10)

def create_button(frame, image, command, text):
    button = tk.Button(frame, image=image, command=command, bg="#282828", bd=0)
    button.pack(side=tk.LEFT, padx=10)
    label = tk.Label(frame, text=text, font=("Arial", 10), bg="#1C1C1E", fg="white")
    label.pack(side=tk.LEFT, padx=10)
    return button

load_button = create_button(button_frame, load_photo, load_music, "Load")
play_button = create_button(button_frame, play_photo, play_music, "Play")
pause_button = create_button(button_frame, pause_photo, pause_music, "Pause")
resume_button = create_button(button_frame, resume_photo, resume_music, "Resume")
stop_button = create_button(button_frame, stop_photo, stop_music, "Stop")
repeat_button = create_button(button_frame, repeat_photo, toggle_repeat, "Repeat")

# Disable buttons initially
play_button.config(state=tk.DISABLED)
pause_button.config(state=tk.DISABLED)
resume_button.config(state=tk.DISABLED)
stop_button.config(state=tk.DISABLED)
repeat_button.config(state=tk.DISABLED)

# Frame for progress bar at the bottom
progress_frame = tk.Frame(root, bg="#1C1C1E")
progress_frame.pack(side=tk.BOTTOM, fill="x", padx=20, pady=20)

current_time_label = tk.Label(progress_frame, text="00:00", font=("Arial", 10), bg="#1C1C1E", fg="white")
current_time_label.pack(side=tk.LEFT, padx=5)

progress = ttk.Progressbar(progress_frame, orient='horizontal', length=400, mode='determinate')
progress.pack(side=tk.LEFT, fill="x", expand=True, padx=10)

total_time_label = tk.Label(progress_frame, text="00:00", font=("Arial", 10), bg="#1C1C1E", fg="white")
total_time_label.pack(side=tk.RIGHT, padx=5)

# Run the application
root.mainloop()
