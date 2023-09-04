import cv2

img = cv2.imread("resources/cat.jpg")

cv2.imshow("Original Image", img)
print(img.shape)
cv2.waitKey(0)

# Resize image
imgResize = cv2.resize(img, (640, 480))
cv2.imshow("Resized Image", imgResize)
print(imgResize.shape)
cv2.waitKey(0)

# Crop image
imgCropped = img[0:600, 0:500]  # height, width
cv2.imshow("Cropped Image", imgCropped)
print(imgCropped.shape)
cv2.waitKey(0)
