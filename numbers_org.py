import cv2
import os

flag=True
rootdir='D:/PyClass/PyCourse-26'
writedir=rootdir+'/numbers'
org=cv2.imread('mnist.png',cv2.IMREAD_GRAYSCALE)
#calculate cells
for i in range(org.shape[0]):
    for j in range(org.shape[1]):
        if org[i,j]>20:
            flag=False
            step=i*10
            break

    if flag==False:
        break

row_count=0
for dir in range(10):
    try:
        os.makedirs(writedir + '/' + str(dir))
        dr = writedir + '/' + str(dir)
    except FileExistsError:
        print('directory exists now !!!!')
        break
    for row in range(dir*step*5,org.shape[0],step):
        row_count += 1
        for col in range(0,org.shape[1],step):
            file=org[row:row+step,col:col+step]
            write = dr + '/' + str(row)+str(col) +str(row_count*row)+ '.jpg'
            cv2.imwrite(write,file)
        if row_count==5:
            row_count=0
            break


