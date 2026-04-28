import cv2
from matplotlib import pyplot as plt

img = cv2.imread("foto-escura.jpg", 0)
imgEqualizada = cv2.equalizeHist(img)
fig = plt.figure(figsize=(10,5))

ax1 = fig.add_subplot(121)
plt.imshow(img, cmap=plt.cm.gray)

ax2 = fig.add_subplot(122)
plt.imshow(imgEqualizada, cmap=plt.cm.gray)

plt.show()