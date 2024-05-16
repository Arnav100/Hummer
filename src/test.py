import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

device_info = sd.query_devices(kind='input')
input_channels = device_info['max_input_channels']
freq = 44100
duration = 5

recording = sd.rec(int(duration * freq), 
                   samplerate=freq, channels=min(input_channels, 2))
sd.wait()
write("recording0.wav", freq, recording)
wv.write("recording1.wav", recording, freq, sampwidth=2)