import cv2
import numpy as np

img = cv2.imread("Resources/cat.jpg")
kernel = np.ones((5, 5), np.uint8)

# # Convert to gray scale image
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image", imgGray)
cv2.waitKey(0)

# Blur image
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)  # (odd, odd)
cv2.imshow("Blurred Image", imgBlur)
cv2.waitKey(0)

# Edge Detection (using canny edge detector)
imgCanny = cv2.Canny(imgGray, 150, 200)  # update the threshold
cv2.imshow("Canny Image", imgCanny)
cv2.waitKey(0)

# Image dialation
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
cv2.imshow("Dialated Image", imgDialation)
cv2.waitKey(0)

# Image Erosion
imgErode = cv2.erode(imgDialation, kernel, iterations=1)
cv2.imshow("Erroded Image", imgErode)
cv2.waitKey(0)
