#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep

def split_str(s, n):
    "split string by its length"
    length = len(s)
    return [s[i:i+n] for i in range(0, length, n)]


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


#serial (['1','2','3','4','5','6','7','8'])
#serial(['1'])
#serial(['2'])
#serial(['3'])
#serial(['1','4','5','7','9','14'])
#sleep(1)
#serial(['9','15'])

