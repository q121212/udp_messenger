#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import time

def insert_text(text):
  if os.path.isfile('log.log'):
    with open('log.log', 'a') as f:
      f.write(time.ctime() + ' ' + text + '\n')
  else:
    with open('log.log', 'w') as f:
      f.write(time.ctime() + ' ' + text + '\n')

if __name__ == '__main__':
  pass