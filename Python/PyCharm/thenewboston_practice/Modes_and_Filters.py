from PIL import Image
from PIL import ImageFilter

crystal = Image.open("Crystal.jpg")
blur = crystal.filter(ImageFilter.BLUR)
detail = crystal.filter(ImageFilter.DETAIL)
edges = crystal.filter(ImageFilter.FIND_EDGES)

crystal.show()
blur.show()
detail.show()
edges.show()