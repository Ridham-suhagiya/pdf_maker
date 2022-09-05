from genericpath import exists
import cv2 as cv
import numpy as np
from glob import glob
import os 

import shutil
import logging
from helper import checker,number
import fpdf
import time





class Pdf_maker:

    def croper(self,testing = False):
        if testing: 
            folder = 'test_images'
            checker('test_images')
        else:
            folder = 'images'
            
        cwd  = os.getcwd()
        cwd1 = os.path.join(cwd,folder)
        # paths = glob(cwd + f"/{folder}/*.png")
        
          
        #      # paths to unprocessed images
            
        # paths += glob(cwd + f"/{folder}/*.jpg")
        # paths += glob(cwd + f"/{folder}/*.jpeg")
        # print(paths)
        
         
        directory  = 'processed_images'
        checker(directory)
        paths = os.listdir('images')
        paths.sort()
        for i,path in enumerate(paths):
            path = os.path.join(cwd1,path)
            print(path)
            
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
            
         
            extension = path.strip().split('.')[-1]
            time.sleep(0.125)
            cv.imwrite(f'{directory}/image-{i}.{extension}',image)
        name = path.split('/')[-1].split('_')[0] + '.pdf'  

        print(cwd)
        return  cwd,name


    def qualityoptimizer(self,testing = False):
        cwd,name = self.croper()

        watermark_path = os.path.join(cwd,'waterMaker/image.png')
        print(watermark_path)
        waterMarkImage = cv.imread(watermark_path)

        waterMarkImage = cv.resize(waterMarkImage,dsize = (800,1128), interpolation=cv.INTER_CUBIC)
        paths = os.listdir('processed_images')
        paths.sort(key = number)
        print(paths)
        for path in paths:
            print(path)
            img_path = os.path.join(cwd, 'processed_images')
            img_path = os.path.join(img_path,path)
            filtered_image = cv.imread(img_path)

            
            gray_mark =  cv.cvtColor(waterMarkImage, cv.COLOR_BGR2GRAY)
            
            _, gray_mark = cv.threshold(gray_mark, 225, 255, cv.THRESH_BINARY_INV)
            gray_mark =gray_mark//25
            # gray_mark = cv.merge([gray_mark,gray_mark,gray_mark])
            
            
            gray = cv.merge([gray_mark,gray_mark,gray_mark])
            b,g,r = cv.split(filtered_image)
            red = cv.merge([r,r,r])

            blue = cv.merge([b,b,b])
            green = cv.merge([g,g,g])
            filtered_image = np.where(((red > gray) & (green > gray) & (blue > gray)),filtered_image - gray,filtered_image)

            
            time.sleep(0.125)
            cv.imwrite(img_path,filtered_image)
        return glob(cwd + "/processed_images/*"),cwd,name

    def pdfmaker(self,testing = False):
        
        pdf = fpdf.FPDF()
        paths,cwd,name = self.qualityoptimizer()
        paths.sort(key = number)
        for i in range(len(paths)):
            pdf.add_page()
            # if t == 1:
            #     name = paths[i].split('/')[-1].split('.')[0] + '.pdf'
            #     t = 0
            


            pdf.image(paths[i],0,0,210,290)
        path = 'static'
        isdir = os.path.isdir(path)
        if not isdir:
            os.makedirs(path)
        else:
            shutil.rmtree(path)
            os.makedirs(path)
        print('ridham')
        if testing :
            pdf.output(f"{path}/test.pdf","F")
            return 'test.pdf'
        else:
            print('ridm')
            pdf.output(f'{path}/{name}','F')
            return name

