import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# 1. Carrega a imagem original
img_color = cv.imread('foto-escura.jpg')

# Verificação de segurança: se a imagem não abrir, o código para aqui
if img_color is None:
    print("Erro ao carregar a imagem. Verifique o nome do arquivo!")
else:
    # 2. Converte de BGR para YUV
    # Y = Luminância (Brilho)
    # U e V = Crominância (Cores)
    yuv = cv.cvtColor(img_color, cv.COLOR_BGR2YUV)

    # 3. Aplica a equalização APENAS no canal Y (índice 0)
    yuv[:, :, 0] = cv.equalizeHist(yuv[:, :, 0])

    # 4. Converte de volta para BGR para que o OpenCV entenda como imagem colorida
    img_output_bgr = cv.cvtColor(yuv, cv.COLOR_YUV2BGR)

    # 5. Prepara as imagens para exibição no Matplotlib (BGR -> RGB)
    img_original_rgb = cv.cvtColor(img_color, cv.COLOR_BGR2RGB)
    img_final_rgb = cv.cvtColor(img_output_bgr, cv.COLOR_BGR2RGB)

    # 6. Visualização com Subplots
    fig = plt.figure(figsize=(10, 5))

    # Imagem Original
    ax1 = fig.add_subplot(221)
    ax1.imshow(img_original_rgb)
    ax1.set_title("Original")
    ax1.axis('off')

    # Imagem Equalizada
    ax2 = fig.add_subplot(222)
    ax2.imshow(img_final_rgb)
    ax2.set_title("Equalizada (Espaço de Cores YUV)")
    ax2.axis('off')

    # Histograma Original (Canais RGB)
    ax3 = fig.add_subplot(223)
    cores = ('red', 'green', 'blue')
    for i, col in enumerate(cores):
        hist = cv.calcHist([img_original_rgb], [i], None, [256], [0, 256])
        ax3.plot(hist, color=col)
    ax3.set_title("Histograma Original")

    # Histograma Final (Canais RGB)
    ax4 = fig.add_subplot(224)
    for i, col in enumerate(cores):
        hist = cv.calcHist([img_final_rgb], [i], None, [256], [0, 256])
        ax4.plot(hist, color=col)
    ax4.set_title("Histograma Equalizado")

    plt.tight_layout() # Ajusta o espaçamento automaticamente
    plt.show()