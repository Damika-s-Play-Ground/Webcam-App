import cv2
import time
import numpy as np
import matplotlib.pyplot as plt

# Open the webcam
capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FPS, 30)

# Increase the exposure time
capture.set(cv2.CAP_PROP_EXPOSURE, 5)

# Set the frame rate
frame_rate = 30

# Initialize a list to store the average brightness values
brightness_values = []

# Initialize a counter to track the elapsed time
elapsed_time = 0
start_time = time.time()

# Loop indefinitely
try:
    while True:
        # Capture a frame from the webcam
        _, frame = capture.read()
    
        # Calculate the average brightness of the frame
        brightness = cv2.mean(frame)[0]
        brightness_values.append(brightness)
    
        # Calculate the elapsed time
        current_time = time.time()
        elapsed_time = current_time - start_time
    
        # If enough time has passed and there are at least two brightness values, calculate the frequency
        if elapsed_time > 1.0 and len(brightness_values) > 10:
            # Use the FFT to analyze the brightness values
            N = len(brightness_values)
            print(brightness_values)
            brightness_fft = np.fft.fft(brightness_values)
            brightness_fft = brightness_fft[:N//2]
            brightness_fft = brightness_fft / np.max(np.abs(brightness_fft))
            frequencies = np.fft.fftfreq(N, d=1/frame_rate)
            frequencies = frequencies[:N//2]
    
            # Find the frequency with the highest power
            # max_power_index = np.argmax(np.abs(brightness_fft))
            # frequency = frequencies[max_power_index]
            # power = np.abs(brightness_fft[max_power_index])
            weighted = frequencies * np.abs(brightness_fft) 
            frequency = np.mean(weighted)
            
    
            # Output the frequency to the screen or file
            print("Frequency: {:.2f} Hz), calculated in {:.2f} sec".format(frequency, elapsed_time))
    
            # Reset the elapsed time counter and the brightness values list
            elapsed_time = 0
            start_time = time.time()
            brightness_values = []
            
        cv2.imshow('video', frame)
        # Check if the user pressed 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    # Release the webcam and close all windows
    capture.release()
    cv2.destroyAllWindows()
