import cv2 as cv

img = cv.imread('')
cv.imshow('dogs',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)


#Simple Thresholding

threshold, thresh = cv.threshold(gray,150,255,cv.THRESH_BINARY)
cv.imshow('simple threshold',thresh)

cv.waitKey(0)