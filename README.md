# 📂 CLI File Organizer

A simple **Python CLI tool** to automatically organize files into folders based on their modification date.

## 🚀 Features
- **Sorts files by modification date** (YYYY-MM format)
- **Interactive mode** (asks before moving each file)
- **Automatically creates folders** if they don't exist
- **Logs all operations** for tracking
- **User-friendly CLI interface**

## 📥 Installation
Requires **Python 3.x**
```sh
# Clone the repository
git clone https://github.com/yourusername/cli-file-organizer.git
cd cli-file-organizer

# Install dependencies (if any in the future)
pip install -r requirements.txt
```

## ▶️ Usage
```sh
python organizer.py
```

## 🔧 How It Works (Single Line Summary)
It asks for a folder location, sorts files into subfolders by modification date, and optionally prompts for confirmation before moving files.

## 📝 Example Run
```
Enter the folder path: /path/to/folder
Enable interactive mode? (y/n): y
Move file1.txt to /path/to/folder/2025-03? (y/n): y
Move image.png to /path/to/folder/2025-02? (y/n): n
Task completed. 1 file moved.
```

## 🛠 Configuration
- **Log File**: All actions are logged in `file_sort_log.txt`
- **Interactive Mode**: Can be toggled on/off at runtime

## 🏗️ Contributing
Feel free to submit issues or PRs!

## 📜 License
MIT License

