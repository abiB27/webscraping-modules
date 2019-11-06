'''useful module to download media from internet'''
import requests
import os
from PIL import Image
import hashlib
import io
import urllib.request
from urllib.parse import urlparse


def image(url) :
    folder_path = path = "C:\\Users\\ABIJITH\\Pictures\\scraped"
    try:
        image_content = requests.get(url).content

    except Exception as e:
        print(f"ERROR - Could not download {url} - {e}")

    try:
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file).convert('RGB')
        file_path = os.path.join(folder_path,hashlib.sha1(image_content).hexdigest()[:10] + '.jpg')
        with open(file_path, 'wb') as f:
            image.save(f, "JPEG", quality=85)
        print(f"SUCCESS - saved {url} - as {file_path}")
    except Exception as e:
        print(f"ERROR - Could not save {url} - {e}")

def name(url) :
    parsed = urlparse(url)
    name =os.path.splitext(os.path.basename(parsed.path))[0]
    return name
