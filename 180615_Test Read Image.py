# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import cv2

# Load an color image in grayscale
img = cv2.imread('BlurEdge.tif',0)
cv2.namedWindow('Window_1', cv2.WINDOW_NORMAL)
cv2.imshow('Window_1',img)
cv2.resizeWindow('Window_1', 600,600)
cv2.waitKey(0)
cv2.destroyAllWindows()

