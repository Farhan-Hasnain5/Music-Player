# Music Player

This is a simple GUI-based music player application built using Python's tkinter library and pygame for audio playback. The application allows users to load, play, pause, resume, stop, and repeat music tracks.

## Features

- Load music files (MP3, WAV)
- Play, pause, resume, and stop music
- Repeat mode for continuous playback
- Progress bar to show the current position of the track
- Display of total duration and current time of the track

## Requirements

- Python 3.x
- tkinter library (usually included with Python)
- pygame library
- Pillow library for image handling

## Installation

1. Clone the repository:
    sh
    git clone https://github.com/Farhan-Hasnain5/Music-Player.git
    cd music-player
    

2. Install the required libraries:
    sh
    pip install pygame pillow
    

## Usage

1. Run the GUI_MusicPlayer.py script:
    sh
    python GUI_MusicPlayer.py
    

2. Use the buttons to control the music playback:
    - *Load*: Load a music file
    - *Play*: Play the loaded music
    - *Pause*: Pause the music
    - *Resume*: Resume the paused music
    - *Stop*: Stop the music
    - *Repeat*: Toggle repeat mode

## Code Overview

- initialize_pygame(): Initializes the pygame mixer.
- load_music(): Loads a music file using a file dialog.
- play_music(): Plays the loaded music and updates the progress bar.
- pause_music(): Pauses the music.
- resume_music(): Resumes the paused music.
- stop_music(): Stops the music and resets the progress bar.
- toggle_repeat(): Toggles the repeat mode.
- check_repeat(): Checks if repeat mode is on and restarts the music if it has ended.
- update_music_length(file_path): Updates the total duration of the loaded music.
- format_time(seconds): Formats time in mm:ss format.
- update_progress_bar(): Updates the progress bar and time labels.
- load_image(image_path): Loads and processes button images.
- create_button(frame, image, command, text): Creates a button with an image and text.
