import os
import shutil
from collections import Counter
from datetime import datetime

# File categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z", ".tar"],
    "Programs": [".exe", ".msi", ".py", ".java", ".cpp", ".c"]
}


def get_category(extension):
    extension = extension.lower()
    for category, extensions in FILE_TYPES.items():
        if extension in extensions:
            return category
    return "Others"


def organize_files(folder_path):
    if not os.path.exists(folder_path):
        print("Invalid folder path!")
        return

    files = [f for f in os.listdir(folder_path)
             if os.path.isfile(os.path.join(folder_path, f))]

    print("\n========== FILE SCAN ==========")
    print("Total Files:", len(files))

    stats = Counter()
    duplicate_counter = Counter(files)

    for file in files:
        print(file)

    print("\nOrganizing files...")

    for file in files:
        source = os.path.join(folder_path, file)

        extension = os.path.splitext(file)[1]
        category = get_category(extension)

        destination_folder = os.path.join(folder_path, category)

        os.makedirs(destination_folder, exist_ok=True)

        destination = os.path.join(destination_folder, file)

        try:
            shutil.move(source, destination)
            stats[category] += 1
        except shutil.Error:
            print(f"File already exists: {file}")
        except PermissionError:
            print(f"Permission denied: {file}")

    print("\n========== STATISTICS ==========")
    print(f"Total Files      : {len(files)}")
    print(f"Images           : {stats['Images']}")
    print(f"Documents        : {stats['Documents']}")
    print(f"Videos           : {stats['Videos']}")
    print(f"Audio            : {stats['Audio']}")
    print(f"Archives         : {stats['Archives']}")
    print(f"Programs         : {stats['Programs']}")
    print(f"Others           : {stats['Others']}")

    print("\n========== SEARCH ==========")

    choice = input("Search by (1) File Name or (2) Extension: ")

    if choice == "1":
        name = input("Enter file name: ").lower()
        found = False
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if name in file.lower():
                    print(os.path.join(root, file))
                    found = True
        if not found:
            print("No file found.")

    elif choice == "2":
        ext = input("Enter extension (example .pdf): ").lower()
        found = False
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.lower().endswith(ext):
                    print(os.path.join(root, file))
                    found = True
        if not found:
            print("No matching extension found.")

    print("\n========== DUPLICATES ==========")

    duplicates = [file for file, count in duplicate_counter.items() if count > 1]

    if duplicates:
        print("Duplicate Files Found:")
        for file in duplicates:
            print(file)
    else:
        print("No Duplicate Files Found.")

    report = os.path.join(folder_path, "file_report.txt")

    with open(report, "w") as f:
        f.write("SMART FILE ORGANIZER REPORT\n")
        f.write("=" * 35 + "\n")
        f.write("Date: " + str(datetime.now()) + "\n")
        f.write("Folder: " + folder_path + "\n\n")

        f.write("Total Files: " + str(len(files)) + "\n\n")

        f.write("Category Statistics\n")
        for key in ["Images", "Documents", "Videos",
                    "Audio", "Archives", "Programs", "Others"]:
            f.write(f"{key}: {stats[key]}\n")

        f.write("\nDuplicate Files\n")

        if duplicates:
            for d in duplicates:
                f.write(d + "\n")
        else:
            f.write("No Duplicate Files Found\n")

        f.write("\nFolder Structure\n")

        for root, dirs, files in os.walk(folder_path):
            level = root.replace(folder_path, "").count(os.sep)
            indent = " " * 4 * level
            f.write(f"{indent}{os.path.basename(root)}/\n")
            subindent = " " * 4 * (level + 1)
            for file in files:
                f.write(f"{subindent}{file}\n")

    print("\nReport Generated Successfully!")
    print("Report saved as:", report)


if __name__ == "__main__":
    try:
        path = input("Enter Folder Path: ").strip()
        organize_files(path)
    except FileNotFoundError:
        print("Folder not found.")
    except PermissionError:
        print("Permission Denied.")
    except Exception as e:
        print("Error:", e)