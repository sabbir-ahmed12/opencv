# Warping Perspective

import cv2
import numpy as np

img = cv2.imread("resources/card.jpg")

width, height = 250, 350
pts1 = np.float32([[513, 136], [942, 297], [306, 696], [697, 855]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOut = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Image", img)
cv2.imshow("Output", imgOut)
cv2.waitKey(0)
