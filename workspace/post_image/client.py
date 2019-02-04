import requests
import cv2
import numpy as np

image_file = ''
url = 'http://127.0.0.1:8000/convert'
files = {'image': open(image_file, 'rb')}
response = requests.post(url, files=files, data={'color_map': 'from_bgr'})

def load_image(data):
    im = np.fromstring(data, np.uint8)
    if im.size != 0:
        return cv2.imdecode(im, cv2.IMREAD_COLOR)
    return None

print(load_image(response.content))