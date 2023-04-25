import pyaudio
import wave

chunk = 1024  # Record in chunks of 1024 samples
sample_format = pyaudio.paInt16  # 16 bits per sample
channels = 2
fs = 44100  # Record at 44100 samples per second
seconds = 10
filename = "output.wav"

p = pyaudio.PyAudio()

# Set the input device to the audio output device
for i in range(p.get_device_count()):
    dev = p.get_device_info_by_index(i)
    if 'CABLE Output' in dev['name']:
        print(dev)
        device_index = dev['index']
        break
device_index=2
stream = p.open(format=sample_format,
                channels=channels,
                rate=fs,
                frames_per_buffer=chunk,
                input=True,
                input_device_index=device_index)

frames = []  # Initialize array to store frames

print("Recording...")

while True:
    data = stream.read(chunk)
    frames.append(data)
    if condition:  # replace with your desired condition
        break

print("Finished recording.")

# Stop and close the stream 
stream.stop_stream()
stream.close()

# Terminate the PyAudio object
p.terminate()

# Save the recorded data as a WAV file
wf = wave.open(filename, 'wb')
wf.setnchannels(channels)
wf.setsampwidth(p.get_sample_size(sample_format))
wf.setframerate(fs)
wf.writeframes(b''.join(frames))
wf.close()
