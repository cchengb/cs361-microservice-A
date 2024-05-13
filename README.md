**Project Overview**
This Flask application generates music dynamically by creating MIDI files based on user-selected musical scales and note counts. The generated MIDI files are then converted to MP3 format for easy listening. This process uses the music21 library for music creation, FluidSynth for MIDI to WAV conversion, and pydub for WAV to MP3 conversion.

**Features**
Generate music by specifying the number of notes and the musical scale.
Automatically convert generated music from MIDI to MP3 format.
Downloadable MP3 files.

**Prerequisites**
Python 3.8+
Flask
music21
FluidSynth
pydub
FFmpeg
A SoundFont file (e.g., GeneralUser GS SoundFont)

**Setup Instructions**
Install Required Python Libraries
Ensure you have Python installed, and then install the necessary Python libraries using pip:
pip install Flask music21 pydub

Install FluidSynth
FluidSynth is used for converting MIDI files to WAV. Installation steps vary by operating system:

For macOS:
brew install fluidsynth

For Ubuntu:
sudo apt-get install fluidsynth

Install FFmpeg
FFmpeg is required by pydub for handling audio formats:
# For macOS
brew install ffmpeg

# For Ubuntu
sudo apt-get install ffmpeg

SoundFont File
Download a SoundFont file, such as the GeneralUser GS, and place it in a directory named soundfonts at the root of your project directory. here's the link: https://www.dropbox.com/s/4x27l49kxcwamp5/GeneralUser_GS_1.471.zip?dl=1

Running the Application
Navigate to the project directory and run the Flask application:
python Music.py

Access the application via a web browser at http://127.0.0.1:5000.

Usage
Select the number of notes and the scale you want to generate music for.
Click "Generate Music" to create and automatically convert the music.
Click on "Download MP3 File" to download the generated music.

Troubleshooting
Ensure all paths and dependencies are correctly set up, especially the path to the SoundFont file in the Music.py script. If there are issues with audio conversion, verify that FluidSynth and FFmpeg are correctly installed and accessible from your environment.
