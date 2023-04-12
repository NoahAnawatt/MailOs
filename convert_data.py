# Dataset file convert HEIC to JPG-3chan/255
from PIL import Image
import os
from sys import argv

assert argv
folder_path = argv[1]

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    filepath = os.path.join(folder_path, filename)

    # Check if the file is not already a JPEG image
    if not filename.endswith(".jpg"):

        # Open the file with Pillow
        with Image.open(filepath) as im:

            # Convert the image to RGB format and save it as a JPEG image
            rgb_im = im.convert("RGB")
            new_filename = os.path.splitext(filename)[0] + ".jpg"
            new_filepath = os.path.join(folder_path, new_filename)
            rgb_im.save(new_filepath)

            # Delete the original file if it is not a JPEG image
            os.remove(filepath)

