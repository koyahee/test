#!/usr/bin/python
# coding: UTF-8

from serial import *

import subprocess, sys

#import LEDctrl

last = 0 # last ct

CHECK_INTERVAL = 10


if len(sys.argv) > 1:
    subprocess.call(['/home/pi/Pimoroni/blinkt/examples/rgb.py','0','0','0'])
    sys.exit(1)

while True:

  ser = Serial('/dev/ttyAMA0',115200)

  line = ser.readline().rstrip()

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
 #       LEDctrl.LED('RED')
        subprocess.call(['/home/pi//Pimoroni/blinkt/examples/rgb.py', '50', '0', '0'])

      else:
 #       LEDctrl.LED('GREEN')
        subprocess.call(['/home/pi/Pimoroni/blinkt/examples/rgb.py', '0', '50', '0'])

    else:
      if last + CHECK_INTERVAL < ct or (last > ct and ct > CHECK_INTERVAL):
#        LEDctrl.LED()
        subprocess.call(['/home/pi/Pimoroni/blinkt/examples/rgb.py', '0', '0', '0'])

  except:
      print "  error"

