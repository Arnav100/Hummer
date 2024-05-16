import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
from data_formatting import convert_to_spectogram
import torch
from model import Net


device_info = sd.query_devices(kind='input')
input_channels = device_info['max_input_channels']
freq = 44100
duration = 10

recording = sd.rec(int(duration * freq), 
                   samplerate=freq, channels=min(input_channels, 2))

print("Begin Humming Now")
sd.wait()
wv.write("recording.wav", recording, freq, sampwidth=2)

img = convert_to_spectogram("recording.wav")

path = "../models/test3.pth"
net = Net()
net.load_state_dict(torch.load(path))
net.eval()
net(img)