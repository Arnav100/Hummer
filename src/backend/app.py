from flask import Flask, request, jsonify, send_from_directory
from main import get_name_of_song

app = Flask(__name__)

# Serve the frontend files
@app.route('/')
def serve_frontend():
    return send_from_directory('../frontend', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('../frontend', path)

@app.route('/upload', methods=['POST'])
def upload():
    if 'audio' not in request.files:
        return jsonify({'error': 'No file part'})

    audio_file = request.files['audio']

    if audio_file.filename == '':
        return jsonify({'error': 'No selected file'})

    # Save the file to a desired location
    audio_file.save('uploaded_audio.wav')
    song_name = get_name_of_song("uploaded_audio.wav")
    return jsonify({'success': 'File uploaded successfully', 'song_name': song_name})

if __name__ == '__main__':
    app.run(port = 5001, debug=True)
