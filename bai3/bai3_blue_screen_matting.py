import cv2
import numpy as np

# Load the background and foreground images
background = cv2.imread('bai3\\background_image.jpg')
foreground = cv2.imread('bai3\\foreground_image.jpg')

# Resize the foreground to match the size of the background
background = cv2.resize(background, (foreground.shape[1], foreground.shape[0]))

# Define blue screen threshold range
lower_green = np.array([90, 0, 0])
upper_green = np.array([110, 255, 255])

# Create blue screen mask
mask = cv2.inRange(foreground, lower_green, upper_green)

# Invert mask to get foreground
foreground = cv2.bitwise_not(foreground, foreground, mask=mask)

# Add foreground and background images
result = cv2.add(foreground, background)

# Display result image
cv2.imshow('Result', result)
# cv2.imwrite('result.jpg', result)
cv2.waitKey(0)
cv2.destroyAllWindows()



