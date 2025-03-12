import os
from PIL import Image

# Define the desired maximum size for the resized images
max_size = (512, 512)

input_dir = "./inputs/"

for filename in os.listdir(input_dir):
  if filename.endswith(('.jpg', '.jpeg', '.png')):  # Adjust for your image types
    filepath = os.path.join(input_dir, filename)

    try:
      img = Image.open(filepath)
      img.thumbnail(max_size)  
      img.save(filepath)
      print(f"Resized and saved: {filename}")
    except IOError as e:
      print(f"Error processing {filename}: {e}")