import cv2 as cv
import numpy as np
from glob import glob
import os

def qualityoptimizer(paths,cwd):

    watermark = os.path.join(cwd,'waterMaker/image.png')
    
    waterMarkImage = cv.imread(watermark)

    waterMarkImage = cv.resize(waterMarkImage,dsize = (800,1128), interpolation=cv.INTER_CUBIC)
    dimensions = []
    for path in paths:
        filtered_image = cv.imread(path)
        # filtered_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        # ret, thresh = cv.threshold(img, 100, 240, cv.THRESH_TOZERO)
        # filtered_image = cv.merge([thresh,thresh,thresh])
        # image_height,image_width,_ = filtered_image.shape
        
        # print(image_height,image_width)
        # if row > image_height :
        #     waterMarkImage = waterMarkImage[:r,:,:]
        # if column > image_width:
        #     waterMarkImage = waterMarkImage[:,:c,:]
        # row,column,_ = waterMarkImage.shape
        # color = (255,255,255)
        # pad = np.full((image_height,image_width, 3), color, dtype=np.uint8)
        
        # dimensions.append((image_height,image_width))
        # center_x = abs(image_height - row )//2
        # center_y = abs(image_width - column)//2
        # pad[center_x:center_x + row, center_y:center_y + column] = waterMarkImage
        
        gray_mark =  cv.cvtColor(waterMarkImage, cv.COLOR_BGR2GRAY)
        
        _, gray_mark = cv.threshold(gray_mark, 225, 255, cv.THRESH_BINARY_INV)
        gray_mark =gray_mark//15
        gray_mark = cv.merge([gray_mark,gray_mark,gray_mark])
        
        
        filtered_image -= gray_mark
        
       
        cv.imwrite(path,filtered_image)
    return glob(cwd + "/processed_images/*")
    