import os
from PIL import Image, ImageDraw
import xml.etree.ElementTree as ET

def convert_inkml_to_jpg(input_folder, output_folder):
    # Certifique-se de que a pasta de saída exista ou crie-a se não existir
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Percorra todos os arquivos na pasta de entrada
    for filename in os.listdir(input_folder):
        if filename.endswith(".inkml"):
            print(f"Processando arquivo: {filename}")
            # Caminho completo do arquivo de entrada
            input_file_path = os.path.join(input_folder, filename)

            # Nome do arquivo de saída (sem extensão)
            output_file_name = os.path.splitext(filename)[0]

            # Caminho completo do arquivo de saída
            output_file_path = os.path.join(output_folder, f"{output_file_name}.jpg")

            # Abra o arquivo InkML e extraia os dados relevantes
            tree = ET.parse(input_file_path)
            root = tree.getroot()
            stroke_data = []
            for trace in root.iter("{http://www.w3.org/2003/InkML}trace"):
                # Limpeza dos pontos e conversão para float
                cleaned_points = [point.strip().split() for point in trace.text.strip().split(',') if point.strip()]
                stroke_data.append([tuple(map(float, point)) for point in cleaned_points])

            # Verifique se há dados de traço
            if stroke_data:
                print(f"Dados de traço encontrados: {stroke_data}")
                # Calcula a largura e a altura da imagem
                min_x = min(coord[0] for stroke in stroke_data for coord in stroke)
                min_y = min(coord[1] for stroke in stroke_data for coord in stroke)
                max_x = max(coord[0] for stroke in stroke_data for coord in stroke)
                max_y = max(coord[1] for stroke in stroke_data for coord in stroke)

                width = int((max_x - min_x) * 100)  # Multiplicamos por 100 para aumentar a resolução
                height = int((max_y - min_y) * 100)  # Multiplicamos por 100 para aumentar a resolução

                # Cria uma nova imagem com a largura e altura calculadas
                image = Image.new('RGB', (width, height), (255, 255, 255))
                draw = ImageDraw.Draw(image)

                # Desenha os traços na imagem
                for stroke in stroke_data:
                    points = [(int((x - min_x) * 100), int((y - min_y) * 100)) for x, y in stroke]
                    draw.line(points, fill=0, width=2)

                # Salva a imagem no formato JPEG
                image.save(output_file_path, "JPEG")

                print(f"Imagem salva em {output_file_path}")

                print(f"Arquivo {filename} convertido com sucesso para {output_file_path}")
            else:
                print(f"Arquivo {filename} não contém dados de traço e não será convertido.")

# Pasta de entrada contendo os arquivos InkML
input_folder = r'C:\Users\J. Lucas\.vscode-cli\Desktop\Natalie\CROHME_training'

# Pasta de saída para os arquivos JPG
output_folder = r'C:\Users\J. Lucas\.vscode-cli\Desktop\Natalie\CROHME_jpg'

# Chame a função para converter os arquivos
convert_inkml_to_jpg(input_folder, output_folder)
