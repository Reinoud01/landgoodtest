from PIL import Image
import os

def compress_image(input_path, target_size_kb=200):
    img = Image.open(input_path)
    
    # Check current size
    file_size_kb = os.path.getsize(input_path) / 1024
    print(f"Current size: {file_size_kb:.2f} KB")
    
    if file_size_kb <= target_size_kb:
        print("Image is already small enough.")
        return

    # Resize if too large (e.g., > 1024px)
    if img.width > 1024:
        ratio = 1024 / img.width
        new_height = int(img.height * ratio)
        img = img.resize((1024, new_height), Image.Resampling.LANCZOS)
        print(f"Resized to 1024x{new_height}")

    # Save with optimization
    output_path = input_path # Overwrite
    quality = 95
    while quality > 10:
        img.save(output_path, "PNG", optimize=True) # PNG doesn't support quality param the same way as JPEG, but optimize helps.
        # If still too big, we might need to resize more or switch to JPEG (but transparency issues).
        # Let's try resizing down if optimization isn't enough.
        
        current_size = os.path.getsize(output_path) / 1024
        print(f"Size with optimize: {current_size:.2f} KB")
        
        if current_size <= target_size_kb:
            print("Target size reached.")
            break
            
        # If optimization didn't work enough, resize down
        width, height = img.size
        new_width = int(width * 0.9)
        new_height = int(height * 0.9)
        img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        print(f"Resizing to {new_width}x{new_height} to reduce size...")
        
if __name__ == "__main__":
    compress_image("src/images/logo.png")
