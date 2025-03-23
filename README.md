### **📂 CLI File Organizer**  
A powerful **Python CLI tool** to automatically organize and manage files into categorized folders based on their type, size, and modification date.  

---

## **🚀 Features**  
✔ **Automatic File Organization** – Sorts files into categories (Programs, Documents, Images, etc.)  
✔ **Custom Categories** – Define your own sorting rules via `config.json`  
✔ **Interactive Mode** – Asks before moving files  
✔ **Undo Last Sort** – Restores files to their original locations  
✔ **Dry Run Mode** – Simulates sorting without making changes  
✔ **Batch Processing** – Sort multiple folders in one command  
✔ **Large File Handling** – Moves big files to a separate folder  
✔ **Ignored Files & Folders** – Skip specific files or directories  
✔ **Multi-Threading** – Sort files faster using multiple threads  
✔ **Sort by Date or Name** – Organize files alphabetically or by modification date  
✔ **Logging** – Save file operations to a log file  
✔ **Estimated Sorting Time** – Displays time taken to sort files  

---

## **📥 Installation**  
Requires **Python 3.x**  
```sh
# Clone the repository
git clone https://github.com/Bhavya312007/cli-file-organizer.git
cd cli-file-organizer

# Install dependencies
pip install tqdm
```

---

## **▶️ Usage**  
```sh
python sorter.py /path/to/folder
```

### **Additional Options:**  
| Command | Description |
|---------|------------|
| `python sorter.py /path/to/folder --interactive` | Asks before moving files |
| `python sorter.py /path/to/folder --dry-run` | Simulates sorting without moving files |
| `python sorter.py --undo` | Restores files to original locations |
| `python sorter.py /path/to/folder --sort-by date` | Sorts files by modification date |
| `python sorter.py /path/to/folder --sort-by name` | Sorts files alphabetically |
| `python sorter.py /path/to/folder --large-files 200` | Moves files above 200MB to "Large Files" folder |
| `python sorter.py /path/to/folder --ignore ".git,node_modules"` | Skips specified files and folders |
| `python sorter.py /folder1 /folder2 --threads 4` | Sorts multiple folders with multi-threading |

---

## **🔧 How It Works (Single Line Summary)**  
The tool scans a given folder, organizes files into appropriate subfolders based on categories, and provides sorting options like date-based, name-based, and size-based sorting.

---

## **📝 Example Run**  
```
$ python sorter.py /home/user/Downloads --interactive
Sorting Files: 100% |██████████| 15/15 files processed
Move report.docx to /home/user/Downloads/Documents? (y/n): y
Move photo.jpg to /home/user/Downloads/Images? (y/n): y
Sorting completed in 2.45 seconds.
```

---

## **🛠 Configuration**  
A `config.json` file is automatically generated if missing and can be customized:  

### **Default Configuration (`config.json`):**  
```json
{
    "categories": {
        "Programs": ["py", "c", "cpp", "java", "exe"],
        "Documents": ["pdf", "docx", "txt", "xls"],
        "Images": ["png", "jpg", "jpeg"],
        "Videos": ["mp4", "mkv", "avi"],
        "Music": ["mp3", "wav"],
        "Archives": ["zip", "rar", "tar"],
        "Large Files": [],
        "Uncategorized": []
    },
    "large_file_size": 100
}
```

### **Configurable Options:**  
- **Custom Categories** – Modify file extensions for each category  
- **Large File Size Threshold** – Change the default file size limit  
- **Ignored Files & Folders** – Exclude specific files and directories  

---

## **🏗️ Contributing**  
Want to improve the script? Feel free to **fork the repo**, make changes, and submit a **pull request**! 🚀  

---

## **📜 License**  
This project is licensed under the **MIT License**.  

---
