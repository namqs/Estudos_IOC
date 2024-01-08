import os
import xml.etree.ElementTree as ET
from svgwrite import Drawing, path

def parse_inkml_file(inkml_file):
    strokes = []
    tree = ET.parse(inkml_file)
    root = tree.getroot()

    for trace in root.findall('.//trace'):
        strokes.append([(float(coord) for coord in stroke.split(',')) for stroke in trace.text.strip().split()])

    return strokes

def convert_to_svg(inkml_dir, svg_dir):
    # Verifica se o diretório de saída existe, se não existir, cria
    if not os.path.exists(svg_dir):
        os.makedirs(svg_dir)

    # Itera sobre os arquivos no diretório de entrada
    for filename in os.listdir(inkml_dir):
        if filename.endswith('.inkml'):
            inkml_path = os.path.join(inkml_dir, filename)
            svg_path = os.path.join(svg_dir, filename.replace('.inkml', '.svg'))

            # Faz o parsing do arquivo InkML
            strokes = parse_inkml_file(inkml_path)

            # Cria um objeto Drawing do svgwrite
            dwg = Drawing(svg_path, profile='tiny')

            # Adiciona os caminhos SVG para cada traço
            for stroke in strokes:
                p = path.Path(stroke=stroke, fill='none', stroke_color='black', stroke_width=2)
                dwg.add(p)

            # Salva o arquivo SVG
            dwg.save()

            # Imprime uma mensagem indicando que a conversão foi realizada com sucesso
            print(f"Converted {inkml_path} to {svg_path}")

# Exemplo de uso
inkml_dir = os.path.join('~/Documentos/FIOCRUZ/dataset', 'CROHME_training')
svg_dir = os.path.join('~/Documentos/FIOCRUZ/dataset', 'CROHME_training_SVG')
convert_to_svg(inkml_dir, svg_dir)


