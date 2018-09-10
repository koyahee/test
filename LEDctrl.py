#!/usr/bin/env python
# -*- coding: utf-8 -*-


import SN74HC595N as sr


def LED(param = None):
  if param is None:
    sr.serial([])
  elif param == 'GREEN':
    sr.serial(['1','2','3','4','5','6','7','8'])
  elif param == 'RED':
    sr.serial(['9','10','11','12','13','14','15','16'])
  else:
    sr.serial(['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16'])

LED()

