from PIL import Image

img = Image.open("src/images/logo.png")
print(f"Width: {img.width}, Height: {img.height}")
