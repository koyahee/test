#!/usr/bin/python
# coding: UTF-8

from serial import *

while True:

  ser = serial.Serial('/dev/ttyAMA0',115200)
  
  line = ser.readline()

  if len(line) > 0 and line[0] == ';':
    print "%s" % line
  else:
    continue
  try:

    lst = line.split(';')
    ct = int(lst[1])

    if len(lst) > 3:
      CHILD_SID = lst[5]

      V = int(lst[6])
      a2 = int(lst[10])

      last = ct

      if V / 2 > a2:
        LEDctrl.LED('RED')

      else:
        LEDctrl.LED('GREEN')

    else:
      if last + 10 < ct or (last > ct and ct > 10): ##10•b’ÊM‚ª–³‚¢ê‡‚ÍÁ“”
        LEDctrl.LED()

  except:
      print "  error"

