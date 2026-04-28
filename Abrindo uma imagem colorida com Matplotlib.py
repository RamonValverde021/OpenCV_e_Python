import cv2 as cv
from matplotlib import pyplot as plt
 
# 1. Carrega a imagem
img = cv.imread('meme.jpg')
 
# 2. Converte de BGR para RGB (Essencial para o Matplotlib)
img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
 
# 3. Exibe usando o pyplot
plt.imshow(img_rgb)
plt.title("Meme - Professor Girafales")
plt.axis('off') # Opcional: remove as coordenadas dos eixos do gráfico
plt.show() 

