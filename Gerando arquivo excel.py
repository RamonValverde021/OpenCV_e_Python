import cv2 as cv
import pandas as pd
import glob

lista_resultados = []
caminhos = glob.glob("fotos_originais/*.jpg")

for p in caminhos:
    img = cv.imread(p, 0) # Carrega em cinza
    if img is not None:
        brilho = img.mean() # Calcula média de brilho com NumPy
        lista_resultados.append({'Arquivo': p, 'Brilho': brilho})
        
if lista_resultados:
    # Transforma a lista de dicionários em um DataFrame elegante
    df_fotos = pd.DataFrame(lista_resultados)

    # Especificando o engine='openpyxl' para evitar ambiguidades
    try:
        # Salva o relatório em Excel exite a biblioteca externa "pip install openpyxl"
        df_fotos.to_excel("relatorio_brilho.xlsx", index=False, engine='openpyxl')
        print("Relatório Excel gerado com sucesso!")
    except ImportError:
        print("Erro: A biblioteca 'openpyxl' não está instalada. Rode 'pip install openpyxl'")
else:
    print("Nenhuma imagem foi encontrada ou processada.")