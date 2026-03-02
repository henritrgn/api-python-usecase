import requests
import zipfile
import os
from urllib.parse import urlparse

def get_unique_name(name, existing_names):
    base, ext = os.path.splitext(name)
    i = 1
    new_name = name
    while new_name in existing_names:
        new_name = f"{base}_{i}{ext}"
        i += 1
    return new_name

zip_name = "downloads.zip"
existing_names = set()

with zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED) as zipf:
    with open("files.txt", "r") as urls:
        for url in urls:
            url = url.strip()
            if not url:
                continue

            print("downloading:", url)

            filename = os.path.basename(urlparse(url).path)
            filename = get_unique_name(filename, existing_names)
            existing_names.add(filename)

            r = requests.get(url, stream=True)
            if r.status_code == 200:
                zipf.writestr(filename, r.content)
            else:
                print("erreur pour", url)

print("OK : Tous les fichiers sont dans", zip_name)