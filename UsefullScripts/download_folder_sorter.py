import os                    # Import the os module to interact with the operating system.
import shutil                # Import the shutil module to perform file operations.
from pathlib import Path     # Import Path from pathlib module for easy path manipulations.

# Define the path to the Downloads folder in the user's home directory.
downloads_path = Path.home() / "Downloads"

# Define a dictionary to categorize files based on their extensions.
file_categories = {
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx"],  # File extensions for documents.
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],              # File extensions for images.
    "Videos": [".mp4", ".avi", ".mov", ".mkv"],                       # File extensions for videos.
    "Music": [".mp3", ".wav", ".aac"],                                # File extensions for music files.
    "Others": []                                                      # No specific extensions, for files that don't match other categories.
}

def create_category_folders():
    """Create category folders in the Downloads directory if they don't exist."""
    for category in file_categories:  # Iterate over each category in the dictionary.
        category_path = downloads_path / category  # Create a path for the category folder.
        category_path.mkdir(exist_ok=True)  # Create the folder, if it doesn't already exist.

def delete_torrents(item):
    """Delete .torrent files from the Downloads directory."""
    # Check if the item is a file and if its extension is .torrent (case insensitive).
    if item.is_file() and item.suffix.lower() == ".torrent":
        print(f"Deleting: {item.name}")  # Print the name of the file being deleted.
        os.remove(item)  # Delete the .torrent file.

def process_file(item):
    """Process each file: delete .torrent files and sort other files into categories."""
    delete_torrents(item)  # Call the delete_torrents function on the current item.
    
    if item.is_file():  # Check if the item is indeed a file.
        moved = False  # Flag to track if the file has been moved.
        
        # Loop through the defined categories and their associated extensions.
        for category, extensions in file_categories.items():
            # Check if the file's extension matches any in the category.
            if item.suffix.lower() in extensions:
                try:
                    print(f"Moving {item.name} to {category} folder.")  # Print moving message.
                    shutil.move(str(item), downloads_path / category / item.name)  # Move the file to the category folder.
                    moved = True  # Mark as moved.
                    break  # Exit the loop since the file has been moved.
                except Exception as e:
                    # Print an error message if moving fails.
                    print(f"Error moving {item.name}: {e}")
        
        # If the file was not moved (not in any listed category), move it to "Others".
        if not moved:
            try:
                print(f"Moving {item.name} to Others folder.")  # Print moving message for "Others".
                shutil.move(str(item), downloads_path / "Others" / item.name)  # Move to "Others".
            except Exception as e:
                # Print an error message if moving fails.
                print(f"Error moving {item.name} to Others: {e}")

def sort_files():
    """Sort files in the Downloads directory."""
    print("Starting to sort files...")  # Indicate that sorting has started.
    
    # Iterate through each item in the Downloads directory.
    for item in downloads_path.iterdir():
        if item.is_dir():  # If the item is a directory.
            print(f"Found directory: {item.name}")  # Print the name of the found directory.
            sort_files_in_directory(item)  # Recursively process files inside the directory.
        else:  # If the item is a file.
            print(f"Processing file: {item.name}")  # Print the name of the file being processed.
            process_file(item)  # Process the file to delete torrents and sort based on type.
    
    print("Sorting complete.")  # Indicate that sorting is finished.

def sort_files_in_directory(directory):
    """Recursively sort files in a given directory."""
    print(f"Processing directory: {directory.name}")  # Print the name of the directory being processed.
    
    for sub_item in directory.iterdir():  # Iterate through items in the subdirectory.
        if sub_item.is_dir():  # If the item is a directory.
            print(f"Found subdirectory: {sub_item.name}")  # Print found subdirectory.
            sort_files_in_directory(sub_item)  # Recursively process files in the subdirectory.
        else:  # If the item is a file.
            print(f"Processing file: {sub_item.name}")  # Print the name of the file being processed.
            process_file(sub_item)  # Process the file to delete torrents and sort based on type.

def main():
    """Main function to initiate sorting."""
    create_category_folders()  # Call the function to create category folders in Downloads.
    sort_files()  # Call the function to sort the files in the Downloads directory.
    print("Files have been sorted.")  # Indicate that all files have been sorted.

# Entry point of the script.
if __name__ == "__main__":
    main()  # Runs the main function when the script is executed.
