from PIL import Image
from PIL import ImageFilter

img1 = Image.open("car.jpg")
img5 = img1.filter(ImageFilter.EDGE_ENHANCE)
img10 = img5.filter(ImageFilter.SHARPEN)
img10.save("outqq.jpg")