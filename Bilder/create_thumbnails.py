from PIL import Image
import os

size = (600, 600)

for pic in os.listdir("."):
    if pic.endswith(".jpeg") or pic.endswith(".jpg"):
        image = Image.open(pic)
        name, extention = os.path.splitext(pic)

        image.thumbnail(size)
        image.save(name + "_thumbnail" + extention)
