import os
import shutil

EXTENSION_MAP = {
    # Images
    ".jpg" : "Image",
    ".jpeg": "Image",
    ".gif" : "Image",
    ".svg" : "Image",
    ".png" : "Image",
    # Audio
    ".mp3" : "Audio",
    ".wav" : "Audio",
    ".flac": "Audio",
    # Documents
    ".txt" : "Document",
    ".pdf" : "Document",
    ".docx": "Document",
    ".xlsx": "Document",
    ".pptx": "Document",
    # Code
    ".py"  : "Code",
    ".js"  : "Code",
    ".html": "Code",
    ".css" : "Code",
    ".java": "Code",
    # Video
    ".mp4" : "Video"
}


def get_all_files(folder_path):
    files = []
    for item in os.listdir(folder_path):
        full_path = os.path.join(folder_path, item)
        if os.path.isfile(full_path):
            files.append(item)
    return files

def get_category(filename):
    name, extension = os.path.splitext(filename)
    return EXTENSION_MAP.get(extension.lower(), "Others")

def create_category_folders(folder_path, categories):
    for item in categories:
        category_path = os.path.join(folder_path, item)
        if not os.path.exists(category_path):
            os.makedirs(category_path)

def move_file(source_path, destination_path):
    shutil.move(source_path, destination_path)

def organize_folder(folder_path):
    files = get_all_files(folder_path)
    categories = set(EXTENSION_MAP.values())
    categories.add("Others")

    create_category_folders(folder_path, categories)

    moved_count = 0
    for filename in files:
        category = get_category(filename)
        source = os.path.join(folder_path, filename)
        destination = os.path.join(folder_path, category, filename)

        name, extension = os.path.splitext(filename)
        counter = 1
        while os.path.exists(destination):
            new_filename = f"{name}_{counter}{extension}"
            destination = os.path.join(folder_path, category, new_filename)
            counter += 1

        move_file(source, destination)
        moved_count += 1
        print(f"Moved: {filename} -> {category}/")

    print(f"--- Done! Total files moved: {moved_count} ---")


if __name__ == "__main__":
    target_dir = input("Enter the path of the folder to organize: ").strip()

    if not os.path.exists(target_dir):
        print("That path doesn't seem to exist. Check your spelling!")
    elif not os.path.isdir(target_dir):               # ✅ FIX: check it's a folder not a file
        print("That path is a file, not a folder. Please enter a folder path.")
    else:
        organize_folder(target_dir)