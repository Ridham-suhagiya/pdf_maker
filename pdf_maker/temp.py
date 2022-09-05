
from os import GRND_RANDOM
import cv2 as cv
import numpy as np



filtered_image = cv.imread('processed_images/image-20.jpg')
og = cv.imread('images/MP-II_ Nuclear Physics_page-0021.jpg')
og = cv.resize(og,dsize = (800,1128), interpolation=cv.INTER_CUBIC)
filtered_image = cv.resize(filtered_image,dsize = (800,1128), interpolation=cv.INTER_CUBIC)
water = cv.imread('waterMaker/image.png')
gray_mark = cv.resize(water,dsize = (800,1128), interpolation=cv.INTER_CUBIC)
gray_mark =  cv.cvtColor(gray_mark, cv.COLOR_BGR2GRAY)

_, gray_mark = cv.threshold(gray_mark, 225, 255, cv.THRESH_BINARY_INV)
gray_mark = gray_mark//20

gray = cv.merge([gray_mark,gray_mark,gray_mark])
b,g,r = cv.split(og)
red = cv.merge([r,r,r])

blue = cv.merge([b,b,b])
green = cv.merge([g,g,g])
filtered_image = np.where(((red > gray) & (green > gray) & (blue > gray)),og - gray,og)



# filtered_image = cv.merge([red,green,blue])
cv.imshow('img',filtered_image[500:])
cv.imshow('og',og[500:])
cv.imshow('water',gray_mark[500:])
cv.waitKey(0)
