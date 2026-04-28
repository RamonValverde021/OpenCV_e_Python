import cv2 as cv
from matplotlib import pyplot as plt

imgOriginal = cv.imread("meme.jpg")

if imgOriginal is None:
    print("Imagem não encontrada!")
else:
    img_rgb = cv.cvtColor(imgOriginal, cv.COLOR_BGR2RGB)

    # CORREÇÃO DO UNPACK: Adicionamos o _ para os canais
    # Lembre-se: shape[0] é altura(linhas), shape[1] é largura(colunas)
    alt, larg, _ = imgOriginal.shape

    # O centro da rotação é (X, Y) -> (largura/2, altura/2)
    centro = (larg / 2, alt / 2)
    
    # Criamos a matriz de rotação (45 graus, escala 1)
    mat = cv.getRotationMatrix2D(centro, 45, 1)

    # Aplicamos a transformação. O tamanho final também é (largura, altura)
    imgRotacionada = cv.warpAffine(img_rgb, mat, (larg, alt))

    fig = plt.figure(figsize=(5, 4))
    plt.imshow(imgRotacionada)
    plt.title("Rotação de 45°")
    plt.axis('off') 
    plt.show()