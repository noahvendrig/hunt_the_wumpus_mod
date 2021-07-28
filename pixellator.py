# from pixellator import Pixellate
# pixellatedImg = Pixellate("path_to_image", size)

from PIL import Image
def Pixellate(imgPath, size):
    path = 'img/mod100.png'
    img = Image.open(imgPath)
    pixImg = img.resize((size,size), Image.BILINEAR)
    result = pixImg.resize(img.size, Image.NEAREST)
    result.save(path)
    # result.show()
    return path

