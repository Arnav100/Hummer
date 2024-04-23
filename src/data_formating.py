from pydub import AudioSegment
from pydub.utils import make_chunks
from transforms import AudioUtil
from PIL import Image
import os


audio_path = "../data/audio/"
specto_path = "../data/spectograms/"

m4a_loc = audio_path + "originals/m4a/"
wav_loc = audio_path + "originals/wav/"

def convert_to_wav():
    for audio in os.listdir(m4a_loc):
        print(audio)
        mp3_file = AudioSegment.from_file(m4a_loc + audio)
        wav_name = audio[:-4] + ".wav"
        # mp3_file.export(wav_loc + wav_name, format="wav")


def split_into_chunk(filename, secs=10):
    folder = audio_path + filename.split("-")[0].lower() 
    name = filename[:-4]
    print("Folder: " + folder)
    song = AudioSegment.from_wav(wav_loc + filename)
    length = secs * 1000
    chunks = make_chunks(song,length)  
    for i, chunk in enumerate(chunks): 
        chunk_name = './' +folder+ '/' + name + "_{0}.wav".format(i) 
        print ("exporting", chunk_name) 

        if len(chunk) < length:
            chunk = chunk + AudioSegment.silent(duration=length - len(chunk))
            
        # chunk.export(chunk_name, format="wav")


def convert_to_spectograms():
    for folder in os.listdir(audio_path):
        if folder == "originals" or not os.path.isdir(audio_path + folder):
            continue
        
        if folder not in os.listdir(specto_path):
            os.makedirs(specto_path + folder)
        
        folder = folder + "/"
        for audio in os.listdir(audio_path + folder):
            aud = AudioUtil.open(audio_path + folder + audio)
            spect = AudioUtil.spectro_gram(aud)
            img = AudioUtil.convert_to_image(spect)
            # Image.fromarray(img, 'RGB').save(specto_path + folder + audio[:-4] + ".jpg")
    
               


if __name__ == "__main__":
    convert_to_wav()
    for filename in os.listdir(wav_loc):
        split_into_chunk(filename)
    convert_to_spectograms()
