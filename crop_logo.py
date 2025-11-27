from PIL import Image

def crop_logo(input_path, output_path):
    img = Image.open(input_path)
    # Crop the bottom part where the text is.
    # Assuming 1024x1024, cropping to 800 height should be safe based on the image.
    # The tree is roughly centered in the top part.
    cropped_img = img.crop((0, 0, 1024, 780)) 
    cropped_img.save(output_path, "PNG")
    print(f"Saved cropped image to {output_path}")

if __name__ == "__main__":
    crop_logo("src/images/logo.png", "src/images/logo.png")
