import cv2

# Open the webcam
capture = cv2.VideoCapture(0)

# Loop indefinitely
while True:
    # Capture a frame from the webcam
    _, frame = capture.read()

    # Display the frame
    cv2.imshow("Webcam", frame)

    # Check if the user pressed 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
capture.release()
cv2.destroyAllWindows()
