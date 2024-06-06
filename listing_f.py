import os
import sys

def list_files_without_extension(directory):
    files_list = []
    # Iterate over all files in the directory
    for file_name in os.listdir(directory):
        # Check if the file is a regular file (not a directory)
        if os.path.isfile(os.path.join(directory, file_name)):
            # Split the file name and extension
            file_name_without_extension, _ = os.path.splitext(file_name)
            # Decode the file name using UTF-8 encoding
            file_name_decoded = file_name_without_extension.encode('utf-8').decode('utf-8')
            files_list.append(file_name_decoded)
    return files_list

# Directory containing the SIGML files
folder_path = r"doc\nouns"

# List all files in the folder without extension
files = list_files_without_extension(folder_path)

# Set encoding for standard output to UTF-8
sys.stdout.reconfigure(encoding='utf-8')

# Print the list of files without extension
for file in files:
    print(file)
