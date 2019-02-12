import pytesseract
import numpy as np
from PIL import Image
import scipy.misc
import cv2
s = ""
for i in range(0, 71):
    img = (str)(i + 1) + ".png"
    im = Image.open(img)
    im_array = np.asarray(im)
    im_inverse = 255 - im_array
    im_result = scipy.misc.toimage(im_inverse)
    new_size = tuple(3 * x for x in im_result.size)
    im = im.resize(new_size, Image.ANTIALIAS)
    s = s + ' ' + pytesseract.image_to_string(im)

print(s)
