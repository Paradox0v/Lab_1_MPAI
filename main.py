import numpy as np
import argparse
from matplotlib import pyplot as plt
from skimage.io import imread, imshow, show, imsave
from skimage.transform import resize
from skimage.exposure import histogram

parser = argparse.ArgumentParser(description= '')
parser.add_argument('-p','--path', type=str, required=True)
parser.add_argument('-a','--axis',type=int, default=0)
parser.add_argument('-r','--result', type=str, required=True)
args = parser.parse_args()

path1 = '0.jpg'
path2 = args.path
img_dog = imread(path1)
img_cat = imread(path2)

img_cat = img_cat/np.max(img_cat)
img_dog = img_dog/np.max(img_dog)

img_cat = resize(img_cat, (img_dog.shape[0], img_dog.shape[1]))

img = np.concatenate((img_dog, img_cat), axis=args.axis, out=None, casting='same_kind')
imsave(args.result+'/result.jpg', img)

fig = plt.figure(figsize=(15, 5))
fig.add_subplot(2, 3, 1)
imshow(img_dog)
fig.add_subplot(2, 3, 2)
imshow(img_cat)
fig.add_subplot(2, 3, 3)
imshow(img)

hist_red, bins_red = histogram(img_dog[:, :, 2])
hist_green, bins_green = histogram(img_dog[:, :, 1])
hist_blue, bins_blue = histogram(img_dog[:, :, 0])

fig.add_subplot(2, 3, 4)
plt.plot(bins_green, hist_green, color='green', linestyle='-', linewidth=1)
plt.plot(bins_red, hist_red, color='red', linestyle='-', linewidth=1)
plt.plot(bins_blue, hist_blue, color='blue', linestyle='-', linewidth=1)

hist_red, bins_red = histogram(img_cat[:, :, 2])
hist_green, bins_green = histogram(img_cat[:, :, 1])
hist_blue, bins_blue = histogram(img_cat[:, :, 0])

fig.add_subplot(2, 3, 5)
plt.plot(bins_green, hist_green, color='green', linestyle='-', linewidth=1)
plt.plot(bins_red, hist_red, color='red', linestyle='-', linewidth=1)
plt.plot(bins_blue, hist_blue, color='blue', linestyle='-', linewidth=1)


hist_red, bins_red = histogram(img[:, :, 2])
hist_green, bins_green = histogram(img[:, :, 1])
hist_blue, bins_blue = histogram(img[:, :, 0])
fig.add_subplot(2, 3, 6)
plt.plot(bins_green, hist_green, color='green', linestyle='-', linewidth=1)
plt.plot(bins_red, hist_red, color='red', linestyle='-', linewidth=1)
plt.plot(bins_blue, hist_blue, color='blue', linestyle='-', linewidth=1)
show()