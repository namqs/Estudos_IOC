import os
import cv2
import numpy as np
import tensorflow as tf
keras = tf.keras
utils = tf.keras.utils
to_categorical = tf.keras.utils.to_categorical

path = 'dataset3'

def carregar_imagens_coloridas(diretorio, tamanho=(64, 64)):
    imagens = []
    rotulos = []
    classes = []  # Lista para armazenar as classes

    for rotulo, classe in enumerate(os.listdir(diretorio)):
        caminho_classe = os.path.join(diretorio, classe)
        classes.append(classe)  # Adiciona a classe à lista
        for arquivo in os.listdir(caminho_classe):
            caminho_imagem = os.path.join(caminho_classe, arquivo)

            # Carregar imagem em cores
            imagem = cv2.imread(caminho_imagem)
            if imagem is not None:
                imagem = cv2.resize(imagem, tamanho)
                imagens.append(imagem)
                rotulos.append(rotulo)

    # Agora, 'classes' contém a lista de classes
    return np.array(imagens), to_categorical(np.array(rotulos)), classes

def carregar_bases_de_dados():
    # Carregar imagens coloridas de treinamento
    diretorio_treinamento = 'dataset3/train'
    imagens_treinamento, rotulos_treinamento, classes = carregar_imagens_coloridas(diretorio_treinamento)

    # Carregar imagens coloridas de teste
    diretorio_teste = 'dataset3/test'
    imagens_teste, rotulos_teste, _ = carregar_imagens_coloridas(diretorio_teste)

    # Normalizar as imagens
    imagens_treinamento = imagens_treinamento / 255.0
    imagens_teste = imagens_teste / 255.0
    return imagens_treinamento, rotulos_treinamento, imagens_teste, rotulos_teste, classes
