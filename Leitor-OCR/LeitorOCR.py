import pytesseract
import cv2

# links uteis:
# corrigir instalação windows: https://stackoverflow.com/questions/50951955/pytesseract-tesseractnotfound-error-tesseract-is-not-installed-or-its-not-i
# instalar outra língua: https://github.com/tesseract-ocr/tessdata
#caminho = r"C:\Users\Python\AppData\Local\Programs\Tesseract-OCR"
#pytesseract.pytesseract.tesseract_cmd = caminho + r'\tesseract.exe'
# pegar linguas: print(pytesseract.get_languages())

imagem = cv2.imread("conta2.jpg")
# Converta a imagem em escala de cinza
gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
# Aplicar limiarização de Otsu
_, binary_image = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# Reduza o ruído com filtro da mediana
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
denoised_image = cv2.medianBlur(binary_image, 3)
# Extraia o texto da imagem pré-processada
texto = pytesseract.image_to_string(denoised_image, lang="por")
print(texto)