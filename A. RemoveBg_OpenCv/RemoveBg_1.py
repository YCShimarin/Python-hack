import cv2
import numpy as np

# Read image
img = cv2.imread('./src/Kevin.jpg', 0)

# Calculate Otsu's threshold value
otsu_thresh, img_threshold = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Display original and inverted thresholded images
cv2.imshow('Original Image', img)
cv2.imshow('Inverted Thresholded Image', img_threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()