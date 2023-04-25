from pydub import AudioSegment
AudioSegment.converter = "C:\\ffmpeg\\ffmpeg\\bin\\ffmpeg.exe"
AudioSegment.ffmpeg = "C:\\ffmpeg\\ffmpeg\\bin\\ffmpeg.exe"
AudioSegment.ffprobe ="C:\\ffmpeg\\ffmpeg\\bin\\ffprobe.exe"
sound1 = AudioSegment.from_file("C:/Users/lenovo/Desktop/Boom Cloud.wav", format="wav")
sound2 = AudioSegment.from_file("C:/Users/lenovo/Desktop/Toy Story.mkv", format="wav")

# sound1 6 dB louder
louder = sound1 + 6


# sound1, with sound2 appended (use louder instead of sound1 to append the louder version)
combined = sound1 + sound2

# simple export
file_handle = combined.export("C:/Users/lenovo/Desktop/Toy Story.mp3", format="mp3")
