# Frequency detecting Webcam app
<p>
This is a simple Python program for testing the frequency and power of a light source in front of your web camera. A high-sensitivity web camera is required for this application. There are a few features to look for when looking for a webcam with higher light sensitivity.
</p>

- checking: Image sensor size: The size of the image sensor in the webcam can affect its sensitivity to light. Webcams with larger image sensors typically have higher sensitivity to light because they can capture more light.

- Pixel size: The size of the pixels on the image sensor can also affect the sensitivity of the webcam to light. Webcams with larger pixels may be more sensitive to light because they can capture more light.

- Sensitivity rating: Some webcams will have a sensitivity rating, which is a measure of the webcam's sensitivity to light. A higher sensitivity rating typically indicates that the webcam is more sensitive to light.

- Low light mode: Some webcams may have a low light mode or other features that can improve the sensitivity of the webcam to light. These features may include things like increased exposure time or the use of larger pixels or a larger image sensor.

<p>
"webcam-frequency-analysis.py" code is designed to detect the frequency of a light source using a webcam and the Fast Fourier Transform (FFT). The code captures frames from the webcam, calculates the average brightness of each frame, and uses the FFT to analyze the brightness values to detect the frequency of the light source.

To test this code, you will need to place the light source in front of the webcam and modulate the intensity of the light source at a consistent frequency. You should then be able to see the frequency of the light source displayed on the screen as the code is running.

If the code is not detecting the frequency of the light source accurately, there may be other issues that you need to address. Some possible issues could include the lighting conditions, the distance between the webcam and the light source, the modulation frequency of the light source, or interference from other light sources. You may need to adjust the code or the light source to address these issues and improve the accuracy of the frequency detection.
</p>
<hr>
Here I'm using several python libraries and you can pip install them by following cmd commands
 
>pip install opencv-python

>pip install numpy

>pip install matplotlib
