from PIL import Image
import os

# Set the folder containing images
image_folder = "."
output_folder = "white_background"

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Process each image
for img_name in os.listdir(image_folder):
    if not img_name.endswith("png") continue
    img_path = os.path.join(image_folder, img_name)
    img = Image.open(img_path).convert("RGBA")

    # Create a white background
    white_bg = Image.new("RGBA", img.size, "WHITE")

    # Composite the image onto the white background
    result = Image.alpha_composite(white_bg, img).convert("RGB")

    # Save processed image
    result.save(os.path.join(output_folder, img_name))
