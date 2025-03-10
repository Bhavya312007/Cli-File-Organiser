import os
import shutil
import datetime

def get_folder_location():
    """Prompt user to enter the folder path and validate it."""
    while True:
        folder_path = input("Enter the folder path: ").strip()
        if os.path.exists(folder_path) and os.path.isdir(folder_path):
            return folder_path
        print("Error: Folder does not exist. Please enter a valid path.")

def sort_files_by_date(folder_path, log_file, interactive):
    """Sorts files into folders based on their modification date."""
    files_moved = 0  # Track number of files moved
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    if not files:
        print("No files found to organize.")
        return

    for file in files:
        file_path = os.path.join(folder_path, file)
        mod_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
        year_month = mod_time.strftime("%Y-%m")  # Format: YYYY-MM

        dest_folder = os.path.join(folder_path, year_month)
        os.makedirs(dest_folder, exist_ok=True)  # Create folder if not exists

        dest_file = os.path.join(dest_folder, file)

        if interactive:
            confirm = input(f"Move {file} to {dest_folder}? (y/n): ").strip().lower()
            if confirm != "y":
                continue

        shutil.move(file_path, dest_file)
        log_action(log_file, f"Moved: {file} -> {dest_folder}")
        files_moved += 1

    print(f"Task completed. {files_moved} files moved.")

def log_action(log_file, message):
    """Logs actions to a file if logging is enabled."""
    if log_file:
        with open(log_file, "a") as log:
            log.write(message + "\n")
    print(message)

def main():
    folder_path = get_folder_location()  # Ask for folder at runtime
    log_file = "file_sort_log.txt"  # Default log file
    interactive = input("Enable interactive mode? (y/n): ").strip().lower() == "y"

    sort_files_by_date(folder_path, log_file, interactive)

if __name__ == "__main__":
    main()
