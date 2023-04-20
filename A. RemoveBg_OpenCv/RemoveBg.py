import cv2
import numpy as np

# Read image
img = cv2.imread('./src/Kevin.jpg', 0)

# Calculate Otsu's threshold value
otsu_thresh, img_threshold = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Set threshold to 0 if lower than minimum human threshold
if otsu_thresh < 5:
    otsu_thresh = 0
    img_threshold = np.zeros_like(img)

# Display original and thresholded images
cv2.imshow('Original Image', img)
cv2.imshow('Otsu Thresholded Image', img_threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()