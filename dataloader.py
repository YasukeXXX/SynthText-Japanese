import ipdb
import h5py
import cv2
import numpy as np
import colorsys
import glob
import json
import os
import random

from imgaug.augmentables.polys import Polygon
from tqdm import tqdm


filename = "./result/SynthText.h5"

h5 = h5py.File(filename, 'r')


def random_colors(N=9, bright=True):
    """
    Generate random colors.
    To get visually distinct colors, generate them in HSV space then
    convert to RGB.
    Borrow from: https://github.com/matterport/Mask_RCNN/blob/master/mrcnn/visualize.py
    """
    brightness = 1.0 if bright else 0.7
    hsv = [(i / N, 1, brightness) for i in range(N)]
    colors = list(map(lambda c: colorsys.hsv_to_rgb(*c), hsv))
    for i, color in enumerate(colors):
        current_color = []
        for channel in color:
            current_color.append(int(channel*255))
        colors[i] = current_color
    random.shuffle(colors)
    return colors


for sample in h5['data']:
    print('Checking file', sample)
    raw_img = h5['data'][sample].value
    word_bb = h5['data'][sample].attrs['wordBB']
    char_bb = h5['data'][sample].attrs['charBB']
    text = h5['data'][sample].attrs['txt']
    for line in text:
        line = line.decode('utf-8')
        print(line)
    char_bb = np.transpose(char_bb, (2, 1, 0))
    word_bb = np.transpose(word_bb, (2, 1, 0))
    colors = random_colors(N=char_bb.shape[0])
    for index, char in enumerate(char_bb):
        current_polygon = Polygon(char)
        raw_img = current_polygon.draw_on_image(
            raw_img, color=colors[index])
    for index, word in enumerate(word_bb):
        current_polygon = Polygon(word)
        raw_img = current_polygon.draw_on_image(
            raw_img, color=colors[index])
        # cv2.putText(raw_img, 'OK', (int(char[0][0]), int(char[0][1]-10)), cv2.FONT_HERSHEY_SIMPLEX, 0.2, (0, 0, 0), lineType=cv2.LINE_AA)
    print(text)
    raw_img = cv2.cvtColor(raw_img, cv2.COLOR_RGB2BGR)
    cv2.imshow('test', raw_img)
    cv2.waitKey(0)
