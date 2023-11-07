from PIL import Image
import os

def add_white_background(input_path, output_path):
    # Open the image
    image = Image.open(input_path)

    # Create a new image with white background
    background = Image.new('RGB', image.size, (100, 100, 100))

    # Check if the image has an alpha channel (transparency)
    if image.mode in ('RGBA', 'LA') or (image.mode == 'P' and 'transparency' in image.info):
        # Convert the image to RGBA mode
        image = image.convert('RGBA')

        # Create a white background image with alpha channel
        background = Image.new('RGBA', image.size, (255, 255, 255, 255))

        # Composite the image onto the white background
        background.paste(image, (0, 0), image)

    else:
        # Paste the image onto the white background
        background.paste(image, (0, 0))

    # Save the resulting image
    try:
         background.save(output_path)
    except Exception as e:
         print(f"An error occurred: {e} ")
  

# Specify the directory containing your images
input_directory = 'uploads'

# Specify the output directory to save the images with white backgrounds
output_directory = 'images_new'

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Iterate through the images in the input directory
for filename in os.listdir(input_directory):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        input_path = os.path.join(input_directory, filename)
        output_path = os.path.join(output_directory, filename)
        add_white_background(input_path, output_path)
