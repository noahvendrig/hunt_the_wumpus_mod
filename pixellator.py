# from pixellator import Pixellate
# pixellatedImg = Pixellate("path_to_image", size)

from PIL import Image
def Pixellate(imgPath, size):
    savePath = 'img/pixellated.png'
    img = Image.open(imgPath)
    pixImg = img.resize((size,size), Image.BILINEAR)
    result = pixImg.resize(img.size, Image.NEAREST)
    result.save(savePath)
    result.show()
    return savePath

pixellatedImgPath = Pixellate("path_to_image", 128)

