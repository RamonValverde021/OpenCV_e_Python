"""import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('meme.jpg', 0)
imgEqualizada = cv.equalizeHist(img)

fig = plt.figure(figsize=(10,3))

ax1 = fig.add_subplot(221)
plt.imshow(img, cmap=plt.cm.gray)

ax2 = fig.add_subplot(222)
plt.imshow(imgEqualizada, cmap=plt.cm.gray)

ax3 = fig.add_subplot(223)
plt.hist(img.ravel(), 256,[0,256], color='gray')

ax4 = fig.add_subplot(224)
plt.hist(imgEqualizada.ravel(), 256,[0,256], color='gray')
plt.show()

plt.show()"""


