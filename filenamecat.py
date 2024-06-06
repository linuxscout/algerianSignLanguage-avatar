import os
import shutil
import docx

# Define paths
base_path = r"C:\wamp64\www\jas\loc2023\doc"
sigml_path = r"C:\wamp64\www\jas\loc2023\sigml"
categories = ["adjectives", "adverbs", "conjunctions", "interjections", "nouns", "prepositions", "pronouns", "verbs"]
docs = {category: os.path.join(base_path, f"{category}.docx") for category in categories}

# Function to read words from a docx file
def read_words_from_docx(doc_path):
    doc = docx.Document(doc_path)
    words = []
    for para in doc.paragraphs:
        words.extend(para.text.split())
    return set(words)

# Read words from each category docx file
category_words = {category: read_words_from_docx(doc_path) for category, doc_path in docs.items()}

# Check and move files
for filename in os.listdir(sigml_path):
    file_without_ext = os.path.splitext(filename)[0]
    file_path = os.path.join(sigml_path, filename)
    for category, words in category_words.items():
        if file_without_ext in words:
            target_folder = os.path.join(base_path, category)
            if not os.path.exists(target_folder):
                os.makedirs(target_folder)
            shutil.move(file_path, target_folder)
            break

print("Files have been moved to the respective folders.")
