import av
import numpy as np
from PIL import ImageGrab

# Set the screen resolution and frame rate
screen_width, screen_height = 1920, 1080
fps = 120

# Set the output video file name and codec
output_file = "output.mp4"
output_codec = "h264"

# Create an output video stream using the specified codec and frame rate
container = av.open(output_file, mode="w")
video_stream = container.add_stream(output_codec, rate=fps)

# Set the video stream parameters (resolution, bit rate, etc.)
video_stream.width = screen_width
video_stream.height = screen_height
video_stream.pix_fmt = "yuv420p"
video_stream.options = {"profile": "high", "level": "4.2"}

# Start recording
for i in range(1000):  # Record 1000 frames
    # Capture a frame from the screen
    img = ImageGrab.grab(bbox=(0, 0, screen_width, screen_height))
    img = np.array(img)

    # Convert the frame to the correct format (RGB -> BGR)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    # Write the frame to the video stream
    packet = video_stream.encode(img)
    container.mux(packet)

# Finalize the output video stream
packet = video_stream.encode(None)
container.mux(packet)

# Close the output video stream and container
container.close()
