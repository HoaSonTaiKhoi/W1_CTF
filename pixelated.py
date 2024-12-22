import hashlib
from PIL import Image
import numpy as np

image1=Image.open("C:\\Code C\\Python_Hash\\hehe\\scrambled1.png")
image2=Image.open("C:\\Code C\\Python_Hash\\hehe\\scrambled2.png")

im1=np.array(image1)*1079
im2=np.array(image2)*1079

answer=np.bitwise_xor(im1, im2).astype(np.uint8)
Image.fromarray(answer).save('C:\\Code C\\Python_Hash\\hehe\\result.png')

image1.close()
image2.close()