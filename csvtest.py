#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv

shoho = []
saiyou = []
pos  =[]

f = open('shoho.csv', 'r')
reader = csv.reader(f)

for row in reader:
  if (row[0] == '201'):
    shoho.append(row[5])

f = open('item_master.csv', 'r')
reader = csv.reader(f)

for row in reader:
  
  if row[0] in shoho:
    pos.append(row[1])


#print shoho
print pos

