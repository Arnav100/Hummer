import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
import torch
from model import Net
from data_formatting import convert_to_spectogram, class_to_song
from time import sleep


def record_audio(save_file="recording.wav"):
    device_info = sd.query_devices(kind='input')
    input_channels = device_info['max_input_channels']
    freq = 44100
    duration = 10
    print("Begin Humming Now in 3...")
    sleep(1)
    print("2...")
    sleep(1)
    print("1...")
    sleep(1)
    print("Go!")
    recording = sd.rec(int(duration * freq), 
                       samplerate=freq, channels=min(input_channels, 2))
    sd.wait()
    wv.write(save_file, recording, freq, sampwidth=2)

def load_model(path):
    print("loading model")
    net = Net()
    net.load_state_dict(torch.load(path))
    net.eval()
    return net

def run_model(net, save_file="recording.wav"):
    print("Converting image")
    img = convert_to_spectogram(save_file)
    img = torch.from_numpy(img).float().permute(2, 1, 0).unsqueeze(0)
    outputs = net(img)
    print(outputs)
    _, predicted = torch.max(outputs.data, 1)
    print(predicted)
    print(class_to_song[predicted.item()])
    return class_to_song[predicted.item()]

def get_name_of_song(save_file="recording.wav"):
    path = "../../models/smaller1.pth"
    net = load_model(path)
    song_name = run_model(net, save_file)
    return song_name

def get_songs():
    return list(class_to_song.values())

if __name__ == "__main__":
    record_audio()
    get_name_of_song()