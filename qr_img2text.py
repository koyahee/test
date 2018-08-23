#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image
import fastzbarlight

file_path = 'camera.jpg'
with open(file_path, 'rb') as image_file:
    image = Image.open(image_file)
    image.load()

codes = fastzbarlight.scan_codes('qrcode', image)
print('QR codes: %s' % codes[0])

