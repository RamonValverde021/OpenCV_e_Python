"""
Desafio:
Você aluno, deve fazer os histogramas 
referentes aos canais de uma imagem colorida (RGB)
"""

# Importa a biblioteca OpenCV para processamento e leitura de imagens
import cv2 as cv
# Importa a biblioteca Matplotlib (módulo pyplot) para plotagem de gráficos
import matplotlib.pyplot as plt

# Carrega a imagem do disco. O OpenCV lê imagens coloridas no formato BGR (Azul, Verde, Vermelho)
img = cv.imread('meme.jpg')

# Separa a imagem carregada em seus 3 canais de cor individuais
azul, verde, vermelho = cv.split(img)

# Cria uma nova figura (janela de exibição) com tamanho de 20 polegadas de largura por 5 de altura
fig = plt.figure(figsize=(20, 5))

# Cria o primeiro espaço para gráfico em uma grade de 1 linha e 3 colunas (posição 1)
ax1 = fig.add_subplot(131)
# Achatamos a matriz do canal azul usando ravel() e criamos o histograma com 256 'bins' no intervalo de 0 a 256
ax1.hist(azul.ravel(), 256, [0,256], color='blue')
ax1.set_title("Histograma do canal azul")

# Cria o segundo espaço na mesma grade (posição 2) para o canal verde
ax2 = fig.add_subplot(132)
ax2.hist(verde.ravel(), 256, [0,256], color='green')
ax2.set_title("Histograma do canal verde")

# Cria o terceiro espaço na mesma grade (posição 3) para o canal vermelho
ax3 = fig.add_subplot(133)
ax3.hist(vermelho.ravel(), 256, [0,256], color='red')
ax3.set_title("Histograma do canal vermelho")

# Mostra todos os gráficos renderizados na tela
plt.show()