from rembg import remove
from PIL import Image

img = Image.open('Kevin_Durant.jpg')

img_without_back = remove(img)

nomeImg = input("Como se chamará a imagem?")

img_without_back.save(nomeImg+'.png')

print("Imagem:", nomeImg+'.png', "salva com sucesso!")