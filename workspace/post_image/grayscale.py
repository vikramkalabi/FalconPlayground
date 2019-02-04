import json

import cv2
import falcon
import numpy as np
from falcon_multipart.middleware import MultipartMiddleware
from loguru import logger


class GrayScale(object):

    def on_get(self, request, respose):
        respose.status = falcon.HTTP_200
        respose.body = json.dumps({
            'message': 'GET request is not supported. Please post an source image (key=`image`)'
        })

    def on_post(self, request, response):
        headers = request.headers
        logger.debug(f'received headers = {json.dumps(headers, indent=4)}')
        image = request.get_param('image')
        image = load_image(image.file.read())
        color_map = request.get_param('color_map')
        logger.debug(f'shape of image received: {image.shape}')
        ret = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        logger.debug(f'shape of image after conversion {ret.shape}')
        response.status = falcon.HTTP_200
        response.data = ret.tobytes()


def load_image(data):
    im = np.fromstring(data, np.uint8)
    if im.size != 0:
        return cv2.imdecode(im, cv2.IMREAD_COLOR)
    return None


app = falcon.API(middleware=[MultipartMiddleware()])
app.add_route('/convert', GrayScale())
