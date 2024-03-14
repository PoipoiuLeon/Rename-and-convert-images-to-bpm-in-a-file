import os
from tkinter import filedialog, Tk
from PIL import Image


def rename_images(folder_path):
    files = os.listdir(folder_path)
    image_files = [f for f in files if is_image_file(os.path.join(folder_path, f))]
    image_counter = 1

    for filename in image_files:
        file_path = os.path.join(folder_path, filename)
        new_name = f"{image_counter}.bmp"
        new_path = os.path.join(folder_path, new_name)
        os.rename(file_path, new_path)
        image_counter += 1


def convert_to_bmp(folder_path):
    files = os.listdir(folder_path)
    image_files = [f for f in files if is_image_file(os.path.join(folder_path, f))]

    for filename in image_files:
        file_path = os.path.join(folder_path, filename)
        with Image.open(file_path) as img:
            img.save(file_path, "BMP")


def is_image_file(filename):
    return filename.lower().endswith(('.png', '.jpeg', '.jpg', '.gif', '.bmp'))


def choose_folder():
    root = Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory(title="Select Folder Containing Images")
    return folder_path

folder_path = choose_folder()

if folder_path:
    rename_images(folder_path)
    convert_to_bmp(folder_path)

    print("Conversion and renaming complete.")
else:
    print("No folder selected. Program terminated.")
