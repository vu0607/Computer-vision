import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('105180399.jpg')

#BGR to HSV
""" HSV_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', HSV_img) """
#BGR to L*a*b
""" lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab) """
# plt.imshow(img)
# plt.show()
# cv.waitKey()
""" RGB_image = cv.cvtColor(img, cv.COLOR_BGR2RGB) """


# Cac thuat toan Blur
bilateral = cv.bilateralFilter(img, 100, 35, 25)

cv.imshow('BILATERAL', bilateral)
cv.waitKey()
