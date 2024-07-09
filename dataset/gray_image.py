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
import shutil
import cv2
from PIL import Image

size = 115, 220


def recursive_listdir(path):
    if not os.path.exists(path):
        print("Target folder does not exist: {}!".format(path))
        return
    target = "{}_{}{}".format(path, size[0], size[1])
    if os.path.exists(target):
        shutil.rmtree(target)
        print("clean old data")
    os.mkdir(target)

    graypath = target+"_gray"
    if os.path.exists(graypath):
        shutil.rmtree(graypath)
        print("clean old data")
    os.mkdir(graypath)

    files = os.listdir(path)
    for file in files:
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path):
            file_name, file_extension = os.path.splitext(file_path)
            if file_extension == ".png":
                #  print("image");
                image = cv2.imread(file_path)
                channels = cv2.split(image)
                if len(channels) == 3:
                    targetfilename = file_path.split('/')

                    gray_img = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

                    image.resize(size)
                    scaleimage=Image.fromarray(image)
                    scaleimage.save(target+"/"+targetfilename[-1])

                    gray = Image.fromarray(gray_img)
                    gray.thumbnail(size, Image.Resampling.LANCZOS)
                    gray.save(graypath+"/"+targetfilename[-1])
                    print(graypath+"/"+targetfilename[-1])
            else:
                print("non-image")
        elif os.path.isdir(file_path):
            recursive_listdir(file_path)


recursive_listdir(
    './CEDAR/signatures/full_forg')
