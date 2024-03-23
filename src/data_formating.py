from pydub import AudioSegment
from pydub.utils import make_chunks
import os


m4a_loc = "../audio/originals/m4a/"
wav_loc = "../audio/originals/wav/"

def convert_to_wav():
    for audio in os.listdir(m4a_loc):
        mp3_file = AudioSegment.from_file(m4a_loc + audio)
        wav_name = audio[:-4] + ".wav"
        mp3_file.export(wav_loc + wav_name, format="wav")


def split_into_chunk(filename, secs=15):
    folder = "../audio/" + filename.split("-")[0].lower() 
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
            
        chunk.export(chunk_name, format="wav")


if __name__ == "__main__":
    convert_to_wav()
    for filename in os.listdir(wav_loc):
        split_into_chunk(filename)
