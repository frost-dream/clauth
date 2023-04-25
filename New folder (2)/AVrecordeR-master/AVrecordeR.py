import cv2
import pyaudio
import wave
import threading
import time
import subprocess
import os
class VideoRecorder():
        def __init__(self):
               self.open = True
               self.fps = 6
	self.fourcc = "MJPG"
	self.frameSize = (640,480)
	self.video_filename = "temp_video.avi"
	self.video_cap = cv2.VideoCapture(0)
	self.video_writer = cv2.VideoWriter_fourcc(*self.fourcc)
	self.video_out = cv2.VideoWriter(self.video_filename, self.video_writer, self.fps, self.frameSize)
	self.frame_counts = 1
	self.start_time = time.time()
        def record(self):
                timer_start = time.time()
	 timer_current = 0
	 while self.open:
                        ret, video_frame = self.video_cap.read()
                        if ret:
		self.video_out.write(video_frame)
		self.frame_counts += 1
		time.sleep(0.16)
                        else:
                                break
	def stop(self):
		if self.open==True:
			self.open=False
			self.video_out.release()
			self.video_cap.release()
			cv2.destroyAllWindows()		
	def start(self):
		video_thread = threading.Thread(target=self.record)
		video_thread.start()
class AudioRecorder():
    def __init__(self):        
        self.open = True
        self.rate = 44100
        self.frames_per_buffer = 1024
        self.channels = 2
        self.format = pyaudio.paInt16
        self.audio_filename = "temp_audio.wav"
        self.audio = pyaudio.PyAudio()
        self.stream = self.audio.open(format=self.format,
                                      channels=self.channels,
                                      rate=self.rate,
                                      input=True,
                                      frames_per_buffer = self.frames_per_buffer)
        self.audio_frames = []
    def record(self):
        self.stream.start_stream()
        while(self.open == True):
            data = self.stream.read(self.frames_per_buffer) 
            self.audio_frames.append(data)
            if self.open==False:
                break
    def stop(self):
        if self.open==True:
            self.open = False
            self.stream.stop_stream()
            self.stream.close()
            self.audio.terminate()
            waveFile = wave.open(self.audio_filename, 'wb')
            waveFile.setnchannels(self.channels)
            waveFile.setsampwidth(self.audio.get_sample_size(self.format))
            waveFile.setframerate(self.rate)
            waveFile.writeframes(b''.join(self.audio_frames))
            waveFile.close()
    def start(self):
        audio_thread = threading.Thread(target=self.record)
        audio_thread.start()
def start_AVrecording(filename):
	global video_thread
	global audio_thread
	video_thread = VideoRecorder()
	audio_thread = AudioRecorder()
	audio_thread.start()
	video_thread.start()
def start_video_recording(filename):
	global video_thread
	video_thread = VideoRecorder()
	video_thread.start()
def start_audio_recording(filename):				
	global audio_thread	
	audio_thread = AudioRecorder()
	audio_thread.start()
def stop_AVrecording(filename):
	audio_thread.stop() 
	frame_counts = video_thread.frame_counts
	elapsed_time = time.time() - video_thread.start_time
	recorded_fps = frame_counts / elapsed_time
	video_thread.stop() 
	while threading.active_count() > 1:
		time.sleep(1)
	if abs(recorded_fps - 6) >= 0.01:
		cmd = "ffmpeg -r " + str(recorded_fps) + " -i temp_video.avi -pix_fmt yuv420p -r 6 temp_video2.avi"
		subprocess.call(cmd, shell=True)
		subprocess.call("ffmpeg -ac 2 -channel_layout stereo -i temp_audio.wav -i temp_video2.avi -pix_fmt yuv420p hello world.avi", shell=True)
	else:
		subprocess.call("ffmpeg -ac 2 -channel_layout stereo -i temp_audio.wav -i temp_video.avi -pix_fmt yuv420p hello world.avi", shell=True)
start_AVrecording('hello world')  
time.sleep(5)
stop_AVrecording('hello world')
