import numpy as np
import cv2
from cv2 import COLOR_BAYER_BG2BGR
# Read the image in Bayer pattern
bayer = cv2.imread('bai2\\input_bayer.png', cv2.IMREAD_GRAYSCALE)

# Apply Malvar-He-Cutler algorithm for demosaicing
demosaiced = cv2.cvtColor(bayer, cv2.COLOR_BAYER_RG2RGB_VNG)

# Display the demosaiced image
cv2.imshow('Demosaiced', demosaiced)
cv2.waitKey(0)
cv2.destroyAllWindows()