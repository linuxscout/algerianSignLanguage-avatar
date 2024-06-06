import os
import json

def list_files_in_categories(base_path):
    categories = {}
    for category in os.listdir(base_path):
        category_path = os.path.join(base_path, category)
        if os.path.isdir(category_path):
            files = [os.path.splitext(f)[0] for f in os.listdir(category_path) if os.path.isfile(os.path.join(category_path, f))]
            categories[category] = files
    return categories

base_path = "doc"  # Change this to your actual base path
categories_files = list_files_in_categories(base_path)

# # Print the dictionary
# for category, files in categories_files.items():
#     print(f"{category}: {files}")

# Save to a JSON file with utf-8 encoding
with open('categories_files.json', 'w', encoding='utf-8') as f:
    json.dump(categories_files, f, ensure_ascii=False, indent=4)
