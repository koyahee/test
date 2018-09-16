#!/usr/bin/python
# coding: UTF-8

from serial import *

import LEDctrl


last = 0 # last ct

CHECK_INTERVAL = 10

while True:

  ser = Serial('/dev/ttyAMA0',115200)

  line = ser.readline().rstrip()
  print line


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
      if last + CHECK_INTERVAL < ct or (last > ct and ct > CHECK_INTERVAL):
        LEDctrl.LED()

  except:
      print "  error"

