import os 
import shutil

def checker(path):
    isdir = os.path.isdir(path)
    if not isdir:
        os.makedirs(path)
    else:
        shutil.rmtree(path)
        os.makedirs(path)


def number(a):
    return int(a.split('-')[-1].split('.')[0])