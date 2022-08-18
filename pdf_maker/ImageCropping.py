import cv2 as cv
import numpy as np
from glob import glob
import os 


def croper(paths,cwd):
    for i,path in enumerate(paths):
        extension = path.strip().split('.')[-1]
        image = cv.imread(path)
        # gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
        row,col,_ =image.shape
        
        if row < 800 or col < 650:
            color = (255,255,255)
            pad = np.full((1128,800, 3), color, dtype=np.uint8)
            center_x = abs(1128 - row )//2
            center_y = abs(800 - col)//2
            
            pad[center_x:center_x + row, center_y:center_y + col] = image
            image = pad
        else:
            image = cv.resize(image,dsize = (800,1128), interpolation=cv.INTER_CUBIC)
        
        
        
        cv.imwrite(f'processed_images/image{i}.{extension}',image)
    return glob(cwd + '/processed_images/*')

