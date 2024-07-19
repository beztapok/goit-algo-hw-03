import os
import shutil

# Функція для створення директорії та генерування файлів

def generate_files(base_dir):
    os.makedirs(base_dir, exist_ok=True)
    
    # Список файлів для створення
    files = [
        "document1.txt", "document2.docx", "spreadsheet1.xlsx", "presentation1.pptx",
        "image1.jpg", "image2.png", "image3.gif", "photo1.bmp",
        "archive1.zip", "script1.py", "audio1.mp3", "video1.mp4"
    ]
    
    # Створення файлів у базовій директорії
    for file in files:
        with open(os.path.join(base_dir, file), 'w') as f:
            f.write(f"Content of {file}")

# Функція для рекурсивного копіювання та сортування файлів

def copy_files_recursively(src, dst):
    try:
        for item in os.listdir(src):
            src_path = os.path.join(src, item)
            if os.path.isdir(src_path):
                copy_files_recursively(src_path, dst)
            else:
                file_extension = os.path.splitext(item)[1].lower().lstrip('.')
                if file_extension in ['txt', 'docx', 'xlsx', 'pptx']:
                    dest_dir = os.path.join(dst, 'doc')
                elif file_extension in ['jpg', 'png', 'gif', 'bmp']:
                    dest_dir = os.path.join(dst, 'pic')
                else:
                    dest_dir = os.path.join(dst, 'other')
                os.makedirs(dest_dir, exist_ok=True)
                shutil.copy2(src_path, os.path.join(dest_dir, item))
    except Exception as e:
        print(f"Error: {e}")

# Головна функція для запуску скрипта
def main():
    base_dir = "dist"
    generate_files(base_dir)
    
    # Шляхи до директорій призначення
    doc_dir = os.path.join(base_dir, 'doc')
    pic_dir = os.path.join(base_dir, 'pic')
    other_dir = os.path.join(base_dir, 'other')
    
    # Створення директорій призначення
    os.makedirs(doc_dir, exist_ok=True)
    os.makedirs(pic_dir, exist_ok=True)
    os.makedirs(other_dir, exist_ok=True)
    
    # Копіювання та сортування файлів
    copy_files_recursively(base_dir, base_dir)
    print("Files have been successfully copied and sorted.")

if __name__ == "__main__":
    main()
