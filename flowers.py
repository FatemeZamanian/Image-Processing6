import cv2
import numpy as np
import argparse
parser=argparse.ArgumentParser()
parser.add_argument('--image')
args=parser.parse_args()
org=cv2.imread(args.image,cv2.IMREAD_GRAYSCALE)
smask=np.zeros((org.shape),dtype='uint8')
for i in range(org.shape[0]):
    for j in range(org.shape[1]):
        if org[i,j]>180:
            smask[i][j]=org[i,j]
blr=cv2.GaussianBlur(org,(51,51),0)
for i in range(1,blr.shape[0]):
    for j in range(1,blr.shape[1]):
        if smask[i,j]>0:
            blr[i,j]=smask[i,j]
blr=cv2.resize(blr,(blr.shape[0]-500,blr.shape[1]-500))
cv2.imshow('c',blr)
cv2.waitKey(0)