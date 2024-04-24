import librosa 
import random
import numpy as np
from scipy.io.wavfile import write
def change_pitch(file):
  audio, samplerate = librosa.load(file, sr=16000)
  for i in range(5):
    steps = random.uniform(-5,5)
    audio_shifted = librosa.effects.pitch_shift(audio, sr = samplerate, n_steps = steps)
    scaled = np.int16(audio_shifted / np.max(np.abs(audio_shifted)) * 32767)
    write('test' + str(i) + '.wav', 44100, scaled)