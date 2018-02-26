# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 15:15:52 2018

@author: schiejak
"""

#project Y image preprocessing

import cv2
import numpy as np
import os
from random import shuffle

cesta_neg = 'G:\\Projekt_Y\\Neg\\'
cesta_poz = 'G:\\Projekt_Y\\Poz\\'

def cropper():
    for i, j in enumerate(os.listdir(cesta_neg)):
        cesta = os.path.join(cesta_neg, j)
        img = cv2.imread(cesta, cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img, (200, 200))
        crop_img = img[15:185, 22:185]
        i = str(i)
        cv2.imwrite('G:\\Projekt_Y\\processed\\Neg\\{}.png'.format(i), crop_img)
    for k, l in enumerate(os.listdir(cesta_poz)):
        cesta = os.path.join(cesta_poz, l)
        img = cv2.imread(cesta, cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img, (200, 200))
        crop_img = img[15:185, 22:185]
        k = str(k)
        cv2.imwrite('G:\\Projekt_Y\\processed\\Poz\\{}.png'.format(k), crop_img)


def loader():
    tr_data = []
    for i in os.listdir(cesta_neg):
        znacka = znackovac(i)
        cesta = os.path.join(cesta_neg, i)
        img = cv2.imread(cesta, cv2.IMREAD_GRAYSCALE)
        tr_data.append([np.array(img), np.array(znacka)])
            
    for i in os.listdir(cesta_poz):
        znacka = znackovac(i)
        cesta = os.path.join(cesta_poz, i)
        img = cv2.imread(cesta, cv2.IMREAD_GRAYSCALE)
        tr_data.append([np.array(img), np.array(znacka)])
    
    shuffle(tr_data)    
    np.save('tr_data.npy', tr_data)
    return tr_data


def znackovac(i):
    znacka = i.split('_')[0]
    if znacka == 'poz':
        return [1,0]
    elif znacka == 'neg':
        return [0,1]
    else:
        print('Nespravny nazev')