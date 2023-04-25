from sounddevice import rec,wait
from scipy.io.wavfile import write
a=rec(10*44100,44100,2)
wait()
write('output.wav',44100,a)
