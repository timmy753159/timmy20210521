from PIL import Image, ImageDraw

newImg = Image.new('RGBA', (300, 300), "Green")
drawObj = ImageDraw.Draw(newImg)
for x in range(100, 200, 3):
    for j in range(100, 200, 3):
        drawObj.point([(x, j)], fill="Red")

drawObj.line([(3, 3), (296, 3),(296, 296), (3,296), (3,3)], fill="blue")
drawObj.line([(5, 5), (294, 5),(294, 294), (5,294), (5,5)], fill="blue")
drawObj.line([(9, 9), (290, 9),(290, 290), (9,290), (9,9)], fill="blue")
for i in range(150, 300, 10):
        drawObj.line([(i, 0), (300, i-150)], fill="Red")


newImg.save("testImg.png")