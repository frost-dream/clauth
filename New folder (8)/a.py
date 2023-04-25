from soundcard import get_microphone,default_speaker
from soundfile import write
with get_microphone(default_speaker().name,True).recorder(100000)as a:
    write('out.wav',a.record(100000*3),100000)
