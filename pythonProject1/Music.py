from flask import Flask, request, jsonify, render_template, send_from_directory, abort
import music21
import random
import os
import subprocess
from pydub import AudioSegment

app = Flask(__name__)

# Set the folder where generated MIDI and MP3 files will be stored
app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'uploads')
sound_font = os.path.join(os.getcwd(), 'soundfonts', 'GeneralUserGs.sf2')  # Path to the SoundFont file

# Ensure the upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

def generate_random_pitch(scale):
    return random.choice(scale)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate')
def generate_music():
    num_notes = int(request.args.get('num_notes', 8))
    scale_type = request.args.get('scale', 'C_major')

    scales = {
        'C_major': ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5'],
        'G_major': ['G3', 'A3', 'B3', 'C4', 'D4', 'E4', 'F#4', 'G4'],
        'A_minor': ['A3', 'B3', 'C4', 'D4', 'E4', 'F4', 'G4', 'A4']
    }

    scale = scales.get(scale_type)
    if not scale:
        return jsonify({"error": "Invalid scale type provided"}), 400

    stream = music21.stream.Stream()
    for _ in range(num_notes):
        pitch = generate_random_pitch(scale)
        note = music21.note.Note(pitch)
        stream.append(note)

    midi_path = os.path.join(app.config['UPLOAD_FOLDER'], 'output.mid')
    stream.write('midi', fp=midi_path)

    # Use FluidSynth to convert MIDI to WAV
    wav_path = midi_path.replace('.mid', '.wav')
    subprocess.run(['fluidsynth', '-ni', sound_font, midi_path, '-F', wav_path, '-r', '44100'], check=True)

    # Convert WAV to MP3 using pydub
    try:
        sound = AudioSegment.from_file(wav_path)
        mp3_path = midi_path.replace('.mid', '.mp3')
        sound.export(mp3_path, format="mp3")
    except Exception as e:
        return jsonify({"error": "Failed to convert MIDI to MP3", "exception": str(e)}), 500

    return jsonify({"message": "Music generated", "file": mp3_path.replace(app.config['UPLOAD_FOLDER'], '/uploads')})

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if not os.path.isfile(file_path):
        abort(404)
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
