import numpy as np
from scipy.io.wavfile import write

rate = 44100
# data = np.random.uniform(-1, 1, rate) # 1 second worth of random samples between -1 and 1
data = np.sin(np.linspace(-np.pi, np.pi, rate))
print(len(data))
scaled = np.int16(data / np.max(np.abs(data)) * 32767)
print(scaled)
write('test.wav', rate, scaled)