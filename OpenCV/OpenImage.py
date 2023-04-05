import cv2 as cv

IMAGE_PATH = 'Images/OpenPicture.jpg'

image = cv.imread(IMAGE_PATH)
cv.imshow('Image', image)

blur = cv.GaussianBlur(image, (1, 1), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

gray = cv.cvtColor(image, cv.COLOR_BGR2HLS)
cv.imshow('Gray', gray)

canny = cv.Canny(image, 125, 125)
cv.imshow('Edges', canny)

dilated = cv.dilate(image, (7, 7), iterations=5)
cv.imshow('Dilated', dilated)

cv.waitKey(0)