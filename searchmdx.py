import os
import shutil

def move_mdx_files(source_dir, target_dir):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    for root, _, files in os.walk(source_dir):
        for file in files:
            if file.endswith(".mdx"):
                source_path = os.path.join(root, file)
                target_path = os.path.join(target_dir, file)

                if os.path.exists(target_path):
                    base, ext = os.path.splitext(file)
                    counter = 1
                    while os.path.exists(target_path):
                        target_path = os.path.join(target_dir, f"{base}_{counter}{ext}")
                        counter += 1

                shutil.move(source_path, target_path)
                print(f"Moved: {source_path} -> {target_path}")

source_directory = "apps"
target_directory = "dev-docs-mdx"
move_mdx_files(source_directory, target_directory)
