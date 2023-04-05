import time
import os
import sys
import cv2

os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

image_path = 'C:/Users/Usuario/Reconhecimento facial/4.jpeg'

#complete the code from the lecture
def read_image(image_path):
  image = Image.open(image_path)
  #convert to RGB, if needed
  image = image.convert('RGB')
  #convert to numpy array
  pixels = np.asarray(image)
  return pixels

#complete the code from the lecture
def display_one_image(one_image, its_label):
  plt.imshow(one_image)
  print("Label =" + its_label)
  print ('image shape: ',one_image.shape)

image = read_image('Images/anis.png')

display_one_image(image, "Anis")

# while True:
#   if cv2.waitKey(1) & 0xFF == 27: 
#     break

print('fim')