import pyaudio
import wave

# Define the audio recording parameters
chunk = 1024
sample_format = pyaudio.paInt16
channels = 2
fs = 44100

# Open a new PyAudio session
p = pyaudio.PyAudio()

# Create a new stream to record audio
stream = p.open(format=sample_format,
                channels=channels,
                rate=fs,
                frames_per_buffer=chunk,
                input=True)

# Create a new wave file to save the recorded audio
frames = []
condition=False
# Record audio until the condition is true
while condition != True:
    if len(frames)>100:
        break
    data = stream.read(chunk)
    frames.append(data)

# Stop recording and close the stream
stream.stop_stream()
stream.close()
p.terminate()

# Save the recorded audio to a file
wf = wave.open("recorded_audio.wav", "wb")
wf.setnchannels(channels)
wf.setsampwidth(p.get_sample_size(sample_format))
wf.setframerate(fs)
wf.writeframes(b"".join(frames))
wf.close()
