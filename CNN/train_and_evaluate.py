from data_loader import carregar_bases_de_dados
from model import construir_rede_neural

def treinar_e_avaliar():
    # Carregar bases de dados
    imagens_treinamento, rotulos_treinamento, imagens_teste, rotulos_teste = carregar_bases_de_dados()

    # Construir a rede neural
    input_shape = (64, 64, 3)  # Ajuste conforme necessário
    rede_neural = construir_rede_neural(input_shape)

    # Treinar a rede neural
    rede_neural.fit(imagens_treinamento, rotulos_treinamento, epochs=20, validation_data=(imagens_teste, rotulos_teste))

    # Avaliar o desempenho do modelo nos dados de teste
    resultado_teste = rede_neural.evaluate(imagens_teste, rotulos_teste)
    print(f"Acurácia nos dados de teste: {resultado_teste[1] * 100:.2f}%")