import numpy as np
import glob
import cv2 as cv
import os
import pandas as pd

index = {}
images = {}

for imagePath in glob.glob(os.getcwd()+'/pre_processamento/*.jpg'):

    filename = imagePath[imagePath.rfind('/')+1:]
    image = cv.imread(imagePath)
    images[filename] = cv.cvtColor(image, cv.COLOR_BGR2RGB)

    hist = cv.calcHist([image], [1, 2], None, [8, 8], [0, 256, 0, 256])
    hist = cv.normalize(hist, hist).flatten()
    index[filename] = hist


print(index)