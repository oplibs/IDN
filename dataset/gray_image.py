#!/usr/bin/python
# -*- coding: utf-8 -*
##############################################################
# File Name: gray_path.py
# Author:
# mail:
# Created Time: Tue Jul  9 09:34:12 2024
# Brief:
##############################################################
import os
import cv2
from PIL import Image

def recursive_listdir(path, target=None):
    files = os.listdir(path)
    for file in files:
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path):
            file_name, file_extension = os.path.splitext(file_path)
            if file_extension==".png":
                #  print("image");
                image = cv2.imread(file_path)
                channels = cv2.split(image)
                if len(channels)==3:
                    gray_img=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
                    gray=Image.fromarray(gray_img)
                    grayfile=file_path.split('/')
                    gray.save(target+"/"+grayfile[-1]);
                    print(target+"/"+grayfile[-1]);
            else:
                print("non-image");
        elif os.path.isdir(file_path):
            recursive_listdir(file_path)

recursive_listdir('./full_org', './full_org_gray')
