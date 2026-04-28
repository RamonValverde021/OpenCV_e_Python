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
    # Converte a imagem de BGR (padrão do OpenCV) para RGB (padrão do Matplotlib)
    img_rgb = cv.cvtColor(imgOriginal, cv.COLOR_BGR2RGB)
    
    # Obtém as dimensões originais da imagem (linhas/altura e colunas/largura)
    totalLinhas, totalColunas, _ = imgOriginal.shape

    # Cria a matriz de translação: deslocamento de 100px em X (direita) e 100px em Y (baixo)
    matriz  = np.float32([[1,0,100],[0,1,100]])
    
    # Aplica a transformação afim (translação) na imagem
    imgDeslocada = cv.warpAffine(img_rgb, matriz, (totalColunas, totalLinhas))

    # Cria uma nova figura no Matplotlib com tamanho de 5x4 polegadas
    fig = plt.figure(figsize=(5, 4))
    # Plota a imagem resultante transladada
    plt.imshow(imgDeslocada)
    # Adiciona um título ao gráfico
    plt.title("Imagem deslocada 100px para baixo e para a direita")
    # Remove a exibição dos eixos (coordenadas) da imagem
    plt.axis('off') 
    # Renderiza e exibe a janela na tela
    plt.show()