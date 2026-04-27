import cv2
import matplotlib.pyplot as plt
 
# Carrega a imagem
imagem = cv2.imread('meme.jpg')
 
# No OpenCV a ordem é BGR (Azul, Verde, Vermelho)
cores = ('b', 'g', 'r')
 
for i, col in enumerate(cores):
    # Calcula o histograma para cada canal
    hist = cv2.calcHist([imagem], [i], None, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])
 
plt.title("Histograma de Cores")
plt.show()
