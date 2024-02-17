import os
import sys
import tkinter as tk
from tkinter import filedialog
import time

def create_symlink(source, destination, is_directory):
    """
    Create a symbolic link from source to destination.
    """
    try:
        if is_directory:
            os.system(f'mklink /d "{destination}" "{source}"')
        else:
            os.system(f'mklink "{destination}" "{source}"')
        print(f"Symlink created successfully: {destination} -> {source}")
        time.sleep(2)  # Keep the console open for 2 seconds after successful job
    except Exception as e:
        print(f"Error creating symlink: {e}")
        input("Press Enter to exit...")  # Wait for user input after error
        sys.exit(1)

def main():
    # Create Tkinter root window for the file dialog
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Prompt user to select destination folder
    destination_folder = filedialog.askdirectory(title="Select Destination Folder")
    if not destination_folder:
        print("No destination folder selected. Exiting.")
        time.sleep(2)  # Keep the console open for 2 seconds before exiting
        sys.exit()

    # Process files/folders passed as arguments
    for arg in sys.argv[1:]:
        # Check if the argument is a valid file/folder
        if os.path.exists(arg):
            is_directory = os.path.isdir(arg)
            file_name = os.path.basename(arg)
            destination_path = os.path.join(destination_folder, file_name)
            create_symlink(arg, destination_path, is_directory)
        else:
            print(f"Invalid file/folder path: {arg}")
            input("Press Enter to exit...")  # Wait for user input after error
            sys.exit(1)

if __name__ == "__main__":
    main()
