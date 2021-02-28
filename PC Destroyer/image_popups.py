import cv2
import random
import os
pic_options = os.listdir('dist/images')
choice = random.randrange(len(pic_options)+1)
print('images\\{}'.format(pic_options[choice-1]))
image = cv2.imread('images\\{}'.format(pic_options[choice-1]))

cv2.imshow('Bruh', image)
while True:
    pass
