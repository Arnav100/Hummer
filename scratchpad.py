
from data.transforms import AudioUtil
import matplotlib.pyplot as plt
from pydub import AudioSegment 
from pydub.utils import make_chunks
import os

# aud = AudioUtil.open("output2.wav")
# spect = AudioUtil.spectro_gram(aud)
# plt.imshow(  spect.permute(1, 2, 0))
# plt.title("Output 2") 
# plt.show()


def split_into_chunk(filename, src, secs=15):
    folder = "audio/" + filename.split("-")[0].lower() 
    name = filename[:-4]
    print("Folder: " + folder)

    song = AudioSegment.from_wav(src + filename)
    length = secs * 1000
    chunks = make_chunks(song,length)  
    for i, chunk in enumerate(chunks): 
        chunk_name = './' +folder+ '/' + name + "_{0}.wav".format(i) 
        print ("exporting", chunk_name) 
        if len(chunk) < length:
            chunk = chunk + AudioSegment.silent(duration=length - len(chunk))
            
        chunk.export(chunk_name, format="wav")

wav_path = "audio/originals/wav/"
for filename in os.listdir(wav_path):
    split_into_chunk(filename, wav_path)