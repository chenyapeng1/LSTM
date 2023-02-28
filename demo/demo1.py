import os
import cv2

path = "./labels"
path3 = "bboxcut"
w = 100
h = 100
img_total = []
txt_total = []
file = os.listdir(path)
for filename in file:
    first,last = os.path.splitext(filename)
    txt_total.append(first)
for img_ in txt_total:
    filename_txt = img_+".txt"
    n = 1
    with open(os.path.join(path,filename_txt),"r+",encoding="utf-8",errors="ignore") as f:
        for line in f:
            aa = line.split(" ")
            

