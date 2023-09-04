import cv2
print("Package Imported")

# Import image
img = cv2.imread("resources/cat.jpg")
cv2.imshow("Cat", img)
cv2.waitKey(0)


# Import video
cap = cv2.VideoCapture("resources/test_video.mp4")

# while loop runs through each frame
while True:
    isSuccess, img = cap.read()
    cv2.imshow("Video", img)
    # wait for the letter 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# Using webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # width
cap.set(4, 480)  # height
cap.set(10, 100)  # brightness

while True:
    isSuccess, img = cap.read()
    cv2.imshow("Webcam", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
