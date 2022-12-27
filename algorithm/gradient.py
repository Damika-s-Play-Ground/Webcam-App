import cv2
import numpy as np


def create_gradient_image(height: int, width: int) -> np.ndarray:
    # Create an image with the given dimensions
    img = np.zeros((height, width, 3), np.uint8)

    # Create a gradient from black to white
    for i in range(height):
        for j in range(width):
            img[i, j] = (j, j, j)

    return img


# Create a gradient image with dimensions 512x512
img = create_gradient_image(512, 512)
# print(img)

# Display the image
cv2.imshow("Gradient", img)
cv2.waitKey(0)

# Close the window
cv2.destroyAllWindows()
