import cv2 as cv
import numpy as np
""" blank = np.zeros((1000,1000,3), dtype='uint8') """
# #Ve 1 tam anh co mau xanh
""" blank[300:1000, 200:1000] = 0,255,0
cv.imshow('Blank', blank) """
# #Ve hinh chu nhat len tam anh
""" cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//3), (0,255,0), thickness=2 ) """

#Ve hinh tron
""" cv.circle(blank,(500,500), radius=100, color=(255,0,255), thickness=2 ) """
#Ve duong
""" cv.line(blank, (0,0), (250,250), (0,255,255), thickness=2 ) """
#Viet text
""" cv.putText(blank, '0,99', (255,255), cv.FONT_HERSHEY_TRIPLEX, 1.0 , (0,255,0), thickness=2) """
# cv.imshow('rectangle', blank)

gray_image = cv.imread("105180399.jpg", 0)
""" canny = cv.Canny(gray_image, threshold1= 100, threshold2= 200) """
# # lam gian anh dilate
""" dilate = cv.dilate(canny, (7,7), iterations=3) """
# cv.imshow("Image edges", dilate)
# Cropping
cropped = gray_image[50:200, 200:400]
cv.imshow('Crop', cropped)
cv.waitKey()
