import sys
import os
import shutil
import logging
import cv2
import tempfile
import shutil
from PIL import Image

# Set up logging
#logging.basicConfig(filename="app.log", level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def get_resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def extract_image(temp_dir):
    image_path = get_resource_path("image.jpg")  # Image inside the EXE
    temp_image_path = os.path.join(temp_dir, "image.jpg")
    shutil.copy(image_path, temp_image_path)
    return temp_image_path

def show_image():
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_image_path = extract_image(temp_dir)
        img = cv2.imread(temp_image_path)
        cv2.imshow("Hidden Image", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
