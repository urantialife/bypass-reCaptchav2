from pydub import AudioSegment

def convert():
	    sound = AudioSegment.from_mp3("/home/chr0m0s0m3s/Downloads/audio.mp3")
	    sound.export("/home/chr0m0s0m3s/Downloads/audio.wav", format="wav") 
