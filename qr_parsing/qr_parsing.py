# coding: utf-8

from pyzbar import pyzbar
from PIL import Image


def parse(image_buffer):
    """Parse qr from the given image and return data as dict
    """
    data = {}
    qr = pyzbar.decode(Image.open(image_buffer))
    if qr and qr[0] and qr[0].data:
        qr_str = str(qr[0].data)
        # Expected data is: key=value&key2=value2...
        parts = qr_str.split('&')
        pairs = [part.split('=', 1) for part in parts]
        data = {k: v for k, v in pairs if k}

    return data
