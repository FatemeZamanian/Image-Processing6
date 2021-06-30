import cv2
import argparse
parser=argparse.ArgumentParser()
parser.add_argument('--image')
args=parser.parse_args()
image=cv2.imread(args.image,cv2.IMREAD_GRAYSCALE)
image = cv2.GaussianBlur(image, (3,3), 3)
cv2.imshow('',image)
cv2.waitKey(0)