from genericpath import exists
import cv2 as cv
import numpy as np
from glob import glob
import os 

import shutil
import logging
from helper import checker
import fpdf






class Pdf_maker:

    def croper(self,testing = False):
        if testing: 
            folder = 'test_images'
        else:
            folder = 'images'
        cwd  = os.getcwd()
        checker('test_images')
        paths = glob(cwd + f"/{folder}/*.png")
            
             # paths to unprocessed images
            
        paths += glob(cwd + f"/{folder}/*.jpg")
        paths += glob(cwd + f"/{folder}/*.jpeg")
        directory  = 'processed_images'
        checker(directory)
        for i,path in enumerate(paths):
            extension = path.strip().split('.')[-1]
            image = cv.imread(path)
            
            row,col,_ =image.shape
            
            if row < 800 and col < 650:
                color = (255,255,255)
                pad = np.full((1128,800, 3), color, dtype=np.uint8)
                center_x = abs(1128 - row )//2
                center_y = abs(800 - col)//2
                logging.debug((row,col))
            
                pad[center_x:center_x + row, center_y:center_y + col] = image
                image = pad
            else:
                image = cv.resize(image,dsize = (800,1128), interpolation=cv.INTER_CUBIC)
            
            
            
            cv.imwrite(f'{directory}/image{i}.{extension}',image)
        return glob(cwd + f'/{directory}/*'), cwd


    def qualityoptimizer(self,testing = False):
        paths,cwd = self.croper(testing)

        watermark = os.path.join(cwd,'waterMaker/image.png')
        
        waterMarkImage = cv.imread(watermark)

        waterMarkImage = cv.resize(waterMarkImage,dsize = (800,1128), interpolation=cv.INTER_CUBIC)
       
        for path in paths:
            filtered_image = cv.imread(path)

            
            gray_mark =  cv.cvtColor(waterMarkImage, cv.COLOR_BGR2GRAY)
            
            _, gray_mark = cv.threshold(gray_mark, 225, 255, cv.THRESH_BINARY_INV)
            gray_mark =gray_mark//15
            gray_mark = cv.merge([gray_mark,gray_mark,gray_mark])
            
            
            filtered_image -= gray_mark
            
        
            cv.imwrite(path,filtered_image)
        return glob(cwd + "/processed_images/*"),cwd

    def pdfmaker(self,testing = False):
        
        pdf = fpdf.FPDF()
        paths,cwd = self.qualityoptimizer(testing)
        t = 1
        name = 'temp.pdf'
        for i in range(len(paths)):
            pdf.add_page()
            if t == 1:
                name = paths[i].split('/')[-1].split('.')[0] + '.pdf'
                t = 0
            


            pdf.image(paths[i],0,0,210,290)
        path = 'static'
        isdir = os.path.isdir(path)
        if not isdir:
            os.makedirs(path)
        else:
            shutil.rmtree(path)
            os.makedirs(path)
        if testing :
            pdf.output(f"{path}/test.pdf","F")
            return 'test.pdf'
        else:
            pdf.output(f'{path}/{name}','F')
            return name