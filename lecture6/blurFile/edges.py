import os
from PIL import Image, ImageFilter

folder = os.path.dirname(__file__)
filepath = os.path.join(folder, "photographer.jpeg")

before = Image.open(filepath)
after = before.filter(ImageFilter.FIND_EDGES)
after.save(os.path.join(folder, "photographer3.jpeg"))