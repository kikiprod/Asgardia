import os
import json
import hashlib

def file_hash(filepath):
    hasher = hashlib.sha256()
    with open(filepath, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

def generate_file_list(directory, base_url):
    file_list = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, directory)
            # Ensure Unix-style paths
            relative_path_unix = relative_path.replace("\\", "/")
            file_list.append({
                "name": relative_path_unix,
                "url": f"{base_url}/{relative_path_unix}",
                "hash": file_hash(file_path),
                "type": "plugins" if "plugins" in relative_path_unix else "config" if "config" in relative_path_unix else "core"
            })
    return file_list

def main():
    directory = "G:/Mon Drive/Valheim Server/CLIENT - Copie/Game/"  # Change this to your BepInEx directory
    base_url = "https://github.com/kikiprod/Asgardia/tree/main/Game"  # Change this to your base URL
    file_list = generate_file_list(directory, base_url)
    output = {"files": file_list}

    with open("files_list.json", "w") as f:
        json.dump(output, f, indent=4)

if __name__ == "__main__":
    main()
