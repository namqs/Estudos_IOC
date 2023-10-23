import cv2
import pytesseract
from PIL import Image

#link util: https://github.com/bdstar/Handwritten-Text-Recognition-Tesseract-OCR

# Carregue a imagem em formato JPEG
imagem_jpg = Image.open('conta2.jpg')

# Salve a imagem em formato PNG
imagem_jpg.save('imagem_convertida.png', 'PNG')

# Abra a imagem em formato PNG
imagem_png = cv2.imread('imagem_convertida.png')

# Converta a imagem em escala de cinza
gray = cv2.cvtColor(imagem_png, cv2.COLOR_BGR2GRAY)

# Aplique um filtro para melhorar o contraste
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
contrast = clahe.apply(gray)

# Reduza o ruído com um filtro da mediana
denoised_image = cv2.medianBlur(contrast, 3)

# Extraia o texto da imagem pré-processada
texto_extraído = pytesseract.image_to_string(denoised_image, lang='por', config='--psm 6')

# Imprima o texto extraído
print(texto_extraído)
