const startRecordingButton = document.getElementById('startRecording');
// const stopRecordingButton = document.getElementById('stopRecording');
const audioPlayer = document.getElementById('audioPlayer');
const countdownTimer = document.getElementById('countdownTimer');
const songName = document.getElementById("songName")
let recorder;
let audioChunks = [];
let countdownInterval;
const RECORDING_TIME = 10; // in seconds

startRecordingButton.addEventListener('click', startRecording);
// stopRecordingButton.addEventListener('click', stopRecording);

function startRecording() {
    navigator.mediaDevices.getUserMedia({ audio: true })
        .then(stream => {
            recorder = new MediaRecorder(stream);
            recorder.start();
            startRecordingButton.disabled = true;
            // stopRecordingButton.disabled = false;
            audioChunks = [];
            countdownTimer.innerText = RECORDING_TIME;

            countdownInterval = setInterval(() => {
                const remainingTime = parseInt(countdownTimer.innerText) - 1;
                countdownTimer.innerText = remainingTime;
                if (remainingTime <= 0) {
                    stopRecording();
                }
            }, 1000);

            recorder.addEventListener('dataavailable', event => {
                audioChunks.push(event.data);
            });

            recorder.addEventListener('stop', () => {
                clearInterval(countdownInterval);
                const audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
                const formData = new FormData();
                formData.append('audio', audioBlob, 'recorded_audio.wav');

                fetch('/upload', {
                    method: 'POST',
                    body: formData
                })
                    .then(response => response.json())
                    .then(data => {
                        console.log(data);
                        song_name = data["song_name"]
                        songName.innerText = song_name
                    })
                    .catch(error => {
                        console.error('Error uploading file:', error);
                    });

                const audioUrl = URL.createObjectURL(audioBlob);
                audioPlayer.src = audioUrl;
            });
        })
        .catch(error => {
            console.error('Error accessing microphone:', error);
        });
}

function stopRecording() {
    if (recorder && recorder.state === 'recording') {
        recorder.stop();
        startRecordingButton.disabled = false;
        // stopRecordingButton.disabled = true;
    }
}
