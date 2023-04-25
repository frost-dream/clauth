import soundcard as sc
import soundfile as sf

output_file_name = 'out.wav'
samplerate = 48000
record_sec = 5
with sc.get_microphone(id=str(sc.default_speaker().name),include_loopback=True).recorder(samplerate=samplerate)as mic:
    data = mic.record(numframes=samplerate*record_sec)
    sf.write(file=output_file_name,data=data[:,0],samplerate=samplerate)
