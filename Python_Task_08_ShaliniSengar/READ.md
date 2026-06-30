# Smart File Organizer

## 📌 Project Title

**Smart File Organizer – File Organizer & Data Management System**

---

## 🎯 Objective

The objective of this project is to develop a real-world automation application using Python that automatically organizes files into different folders based on their file extensions. This project helps in understanding file handling, directory management, object-oriented programming, exception handling, and automation concepts.

---

## 🚀 Features

* Accepts a folder path from the user.
* Verifies whether the directory exists.
* Scans all files in the selected directory.
* Displays total files, file names, and extensions.
* Automatically creates categorized folders.
* Organizes files based on their extensions.
* Generates file statistics.
* Searches files by name or extension.
* Detects duplicate files.
* Generates a detailed report (`file_report.txt`).
* Handles exceptions gracefully.
* Prevents application crashes due to invalid operations.

---

## 📂 File Categories

The application organizes files into the following folders:

* Images
* Documents
* Videos
* Audio
* Archives
* Programs
* Others

---

## 🛠️ Modules Implemented

### Module 1: Directory Selection

* Takes folder path as input.
* Validates directory existence.

### Module 2: File Scanning

* Scans all files inside the selected folder.
* Displays file details.

### Module 3: Automatic File Organization

* Creates category folders automatically.
* Moves files according to their extensions.

### Module 4: File Statistics

* Displays:

  * Total Files
  * Images
  * Documents
  * Videos
  * Audio Files
  * Unknown Files

### Module 5: Search Functionality

* Search files by:

  * File Name
  * File Extension

### Module 6: Duplicate File Detection

* Identifies duplicate file names in the directory.

### Module 7: Report Generation

Generates a report named:

`file_report.txt`

The report contains:

* Date
* Folder Name
* Total Files
* Category-wise Count
* Duplicate Files
* Organized Folder Structure

### Module 8: Exception Handling

Handles exceptions such as:

* Invalid Folder Path
* Permission Denied
* File Already Exists
* Missing Folder

---

## 💻 Technologies Used

* Python 3
* Object-Oriented Programming (OOP)
* File Handling
* Exception Handling
* `os` Module
* `shutil` Module
* `datetime` Module
* Collections Module

---

## ▶️ How to Run

1. Clone the repository:

```bash
git clone <your-github-repository-link>
```

2. Navigate to the project folder:

```bash
cd Python_Task_08_ShaliniSengar
```

3. Run the program:

```bash
python smart_file_organizer.py
```

4. Enter the folder path when prompted.

Example:

```text
Enter Folder Path:
C:\Users\Shalini\Downloads
```

---

## 📸 Screenshots

Add screenshots of:

1. Folder selection.
2. File scanning output.
3. Organized folders.
4. Statistics display.
5. Duplicate detection.
6. Generated report.

---

## ⚠️ Challenges Faced

* Handling invalid folder paths.
* Managing file movement without overwriting existing files.
* Detecting duplicate files efficiently.
* Categorizing files with different extensions.
* Implementing proper exception handling.

---

## 🔮 Future Improvements

* Add GUI using Tkinter.
* Implement progress bar.
* Export reports to CSV format.
* Add dark mode support.
* Detect duplicate files based on content.
* Sort files by size.
* Add empty folder detection.
* Implement recently modified files feature.

---

## 📁 Project Structure

```text
Python_Task_08_ShaliniSengar/
│
├── smart_file_organizer.py
├── file_report.txt
├── Sample_Test_Folder/
├── Screenshots/
├── README.md
└── Project_Report.pdf
```

---

## 👩‍💻 Author

**Shalini Sengar**

Python Internship Task 08
White Band Associates
