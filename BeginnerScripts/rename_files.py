import os
from PIL import Image
from PIL.ExifTags import TAGS
import shutil

def get_date_taken(path):
    """Extract the date taken from the image metadata."""
    try:
        image = Image.open(path)
        exif_data = image._getexif()
        if not exif_data:
            return None
        for tag, value in exif_data.items():
            tag_name = TAGS.get(tag, tag)
            if tag_name == 'DateTimeOriginal':
                return value.replace(':', '').replace(' ', '_')
    except Exception as e:
        print(f"Error reading {path}: {e}")
        return None

def rename_images_in_folder(folder_path):
    """Rename all image files in a folder to their metadata date."""
    if not os.path.exists(folder_path):
        print("The specified folder does not exist.")
        return

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            date_taken = get_date_taken(file_path)
            if date_taken:
                file_extension = os.path.splitext(filename)[1]
                new_name = f"{date_taken}{file_extension}"
                new_path = os.path.join(folder_path, new_name)
                if not os.path.exists(new_path):  # Avoid overwriting files
                    os.rename(file_path, new_path)
                    print(f"Renamed {filename} to {new_name}")
                else:
                    print(f"File {new_name} already exists. Skipping.")

# Usage example:
folder_path = 'path/to/your/folder'  # Replace with the path to your folder
rename_images_in_folder(folder_path)