from PIL import Image

src = Image.open("IMG_0737.jpg")
square_src = src.resize((300,300))
flip_src = src.transpose(Image.FLIP_LEFT_RIGHT)
spin_src = src.transpose(Image.ROTATE_270)


src.show()
square_src.show()
flip_src.show()
spin_src.show()