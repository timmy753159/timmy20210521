from PIL import Image
from PIL import ImageFilter

img1 = Image.open("lol.jpg")
img2 = img1.filter(ImageFilter.BLUR) #模糊化
img2.save("out1.jpg")
img3 = img1.filter(ImageFilter.CONTOUR)
img3.save("out2.jpg")
img4 = img1.filter(ImageFilter.DETAIL)
img4.save("out3.jpg")
img5 = img1.filter(ImageFilter.EDGE_ENHANCE) #物件邊緣增強
img5.save("out4.jpg")
img6 = img1.filter(ImageFilter.EDGE_ENHANCE_MORE)
img6.save("out5.jpg")
img7 = img1.filter(ImageFilter.EMBOSS)
img7.save("out6.jpg")
img8 = img1.filter(ImageFilter.FIND_EDGES)
img8.save("out7.jpg")
img9 = img1.filter(ImageFilter.SMOOTH)
img9.save("out8.jpg")
img10 = img1.filter(ImageFilter.SHARPEN)
img10.save("out9.jpg")