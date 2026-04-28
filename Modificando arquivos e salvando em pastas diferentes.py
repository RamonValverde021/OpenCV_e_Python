import cv2 as cv
import os
import glob

# 1. Definimos a pasta de origem e destino
pasta_origem = "fotos_originais"
pasta_destino = "resultados_processados"

# 2. Usamos o OS para garantir que a pasta de destino exista
if not os.path.exists(pasta_destino):
    os.makedirs(pasta_destino)

# 3. Usamos o GLOB para pegar apenas os arquivos JPG
fotos = glob.glob(os.path.join(pasta_origem, "*.jpg"))

for caminho in fotos:
    # 4. Usamos o OS para extrair apenas o nome do arquivo (sem a pasta)
    nome_base = os.path.basename(caminho)
    
    # Processamento OpenCV
    img = cv.imread(caminho)
    if img is not None:
        cinza = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        
        # 5. Criamos o novo caminho de salvamento
        caminho_salvamento = os.path.join(pasta_destino, "cinza_" + nome_base)
        cv.imwrite(caminho_salvamento, cinza)
        print(f"Arquivo {nome_base} processado e salvo!")