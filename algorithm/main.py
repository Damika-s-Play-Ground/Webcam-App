import cv2
import time
import numpy as np
from hazard_detect import is_hazardous

# Buffer size (in frames)
BUFFER_SIZE = 8

# Open the webcam
cap = cv2.VideoCapture(0)

# Disable auto exposure
# TODO: This is not working

# Reduce camera resolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_WIDTH//4)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FRAME_HEIGHT//4)

# Width and height of the webcam frame
WIDTH = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
HEIGHT = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Set the quarter area threshold (in pixels)
quarter_area_threshold = (WIDTH * HEIGHT) / 4

# Initialize the frame buffer
frame_buffer = []

# Initialize previous time
prev_time = time.time()


# Capture frames from the webcam
try:
    while True:
        # Read a frame from the webcam
        ret, frame = cap.read()
    
        # If the frame was successfully read
        if ret:
            # Add the frame to the frame buffer
            frame_buffer.append(frame)
    
            # If the frame buffer has at least 8 frames
            if len(frame_buffer) >= BUFFER_SIZE:
    
                # Get the current FrameSlidingWindow
                frame_sliding_window = frame_buffer[-BUFFER_SIZE:]
    
                # For each pixel location in frame
                for j in range(1, BUFFER_SIZE):
                    # Initialize the flashing pixels count
                    flashing_pixels_count = 0
                    # Get the current and previous frames
                    cur_frame = frame_sliding_window[j]
                    prev_frame = frame_sliding_window[j-1]
    
                    # For each pixel in frame
                    # for k in range(frame.shape[0]):  # TODO: This is too slow
                    #     for l in range(frame.shape[1]):
                    #         if is_hazardous(cur_frame[k][l] / 255, prev_frame[k][l] / 255):
                    #             flashing_pixels_count += 1
                    flashing_pixels_count = np.sum(is_hazardous(cur_frame / 255, prev_frame / 255))
                    if (flashing_pixels_count > quarter_area_threshold):
                        print("Flashing detected")
                        
                print("Frame processed")
                
except KeyboardInterrupt:
    cap.release()
    cv2.destroyAllWindows()
    
