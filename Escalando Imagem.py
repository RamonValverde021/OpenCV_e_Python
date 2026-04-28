import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# Carrega a imagem do disco
imgOriginal = cv.imread("meme.jpg")

# Verifica se a imagem foi carregada corretamente
if imgOriginal is None:
    # Exibe mensagem de erro caso o arquivo não seja encontrado
    print("Imagem não encontrada!")
else:
    imgModificada = cv.resize(imgOriginal,
                         None,
                         fx = 0.8,
                         fy = 0.8,
                         interpolation = cv.INTER_CUBIC) # INTER_NEAREST, INTER_LINEAR, INTER_AREA, INTER_CUBIC

    cv.imshow("Imagem Original", imgOriginal)
    cv.imshow("Imagem Modificada", imgModificada)
    # Aperta ESC para fechar as janelas
    cv.waitKey(0)
    cv.destroyAllWindows()