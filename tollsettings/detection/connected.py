import cv2
import numpy as np
#import pytesseract
im=cv2.imread('2.png',0)
#pytesseract.pytesseract.tesseract_cmd = r"C:\\Users\\user\\AppData\\Local\\Tesseract-OCR\\tesseract.exe"
#config = ('-l eng --oem 1 --psm 3')
#
#text = pytesseract.image_to_string(image)

from skimage import measure
from skimage import filters
import matplotlib.pyplot as plt
import numpy as np


all_labels = measure.label(im)
blobs_labels = measure.label(im, background=0)

plt.figure(figsize=(9, 3.5))
plt.subplot(131)
plt.imshow(im, cmap='gray')
plt.axis('off')
plt.subplot(132)
plt.imshow(all_labels, cmap='nipy_spectral')
plt.axis('off')
plt.subplot(133)
plt.imshow(blobs_labels, cmap='nipy_spectral')
plt.axis('off')

plt.tight_layout()
plt.show()


