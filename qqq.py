from PIL import Image
from PIL import ImageFilter

img1 = Image.open("car.jpg")
img5 = img1.filter(ImageFilter.EDGE_ENHANCE)

img5.save("outqq.jpg")