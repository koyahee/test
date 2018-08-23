#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import time
import picamera
import zbar

import csv
from copy import copy

import signal
import sys

from time import sleep

def split_str(s, n):
    "split string by its length"
    length = len(s)
    return [s[i:i+n] for i in range(0, length, n)]

def handler(signal, frame):
  sys.exit(0)

#item_id_array_cache = []

def get_pos(item_id_array):
  print item_id_array
#  global item_id_array_cache
#  if item_id_array_cache == item_id_array:
#    return None

#  item_id_array_cache = copy(item_id_array)
  
  pos = []
  
  f = open('item_master.csv', 'r')
  reader = csv.reader(f)

  for row in reader:
    
    if row[0] in item_id_array:
      pos.append(row[1])


  #print item_id_array
#  print pos

  return pos

def beep():

  import RPi.GPIO as GPIO
  from time import sleep

  SOUNDER = 21
  Hz = 850

  GPIO.setmode(GPIO.BCM)
  GPIO.setup(SOUNDER, GPIO.OUT, initial = GPIO.LOW)

  p = GPIO.PWM(SOUNDER, 1)

  p.start(50)

  p.ChangeFrequency(Hz)
  sleep(0.1)

  p.stop()
  GPIO.cleanup()

def serial(arr):

  import wiringpi
  import math

  #pin raspi 74HC595
  #MOSI= 19 #SDI
  #CLK = 23 #SCK
  #CE0 = 24 #LATCH

  SPI_Ch= 0 #CE0
  SPI_Speed = 100000

  # initialization
  print("Initialization...")
  wiringpi.wiringPiSPISetup (SPI_Ch, SPI_Speed)

  num_items = 16
  data = ''
  bit =''

  for i in range(num_items):
    if str(i + 1) in arr:
      bit = bit + '1'
    else:
      bit = bit + '0'

  print bit

  bit_array = split_str(bit, 8) 
    
  for row in bit_array:
    data = data + chr(int(row, 2))

  wiringpi.wiringPiSPIDataRW(SPI_Ch, data)

  print("done")


from PIL import Image

scanner = zbar.ImageScanner()
scanner.parse_config('enable')

signal.signal(signal.SIGINT, handler)

while True:

    # Create the in-memory stream
    stream = io.BytesIO()
    with picamera.PiCamera() as camera:
    #    camera.start_preview()
    #    time.sleep(2)
#        camera.resolution = (2592, 1944)
#        camera.resolution = (1920, 1080)
        camera.resolution = (1024, 768)
        camera.capture(stream, format='jpeg')
    # "Rewind" the stream to the beginning so we can read its content
    stream.seek(0)
    pil = Image.open(stream).convert('L')
    (width, height) = pil.size

    # Return image as a bytes object
    raw = pil.tobytes()

    # The Y800 color format is an 8 bit monochrome format.
    image = zbar.Image(width, height, 'Y800', raw)

    # scan the image for barcodes
    scanner.scan(image)

    for symbol in image:
#      print 'decoded', symbol.type, 'symbol', '"%s"' % symbol.data

      item_id_array = []

#      print '%s' % symbol.data.split()

      for row in csv.reader(symbol.data.split()):
        if (row[0] == '201'):
          item_id_array.append(row[5])
      
      pos_arr = get_pos(item_id_array)
      
      serial(pos_arr)

      beep()


