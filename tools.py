#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import os
from time import sleep
from random import randint,choice
#from gi.repository import Notify
#import threading  # Threading module itself 
#import thread

"""
Functions Summary:
 - draw_notify: Send Desktop notification
 - notify: wrapper for draw_notify for implementing duration of notification
 - internet: Check if connected to the internet
 - get_public_IP: Get current public IP address
 - is_IP(ip): check if a string has IPv4 format (int.int.int.int)
 - files: list files in folder
 - folders: list subfolders in folder
"""

#def draw_notify(summary='ALERT!',body='Do the thing',dur=2):
#   """
#     Shows a desktop notification
#     Dependencies:
#        sudo apt-get install python-gobject libnotify-bin
#   """
#   Notify.init("Notificator")
#   # Create the notification object
#   # icon = "/path/to/icon.png"
#   notification = Notify.Notification.new(summary,body)
#   notification.show()
#   sleep(dur)
#   notification.close()
#
#
#def notify(summary='ALERT!',body='Do the thing',dur=2,wait=False):
#   """
#     Wrapper for the notification function. Implements the option for not
#   waiting until the notification expires.
#   """
#   if wait:
#      draw_notify(summary,body,dur)
#   else:
#      t = threading.Thread(target=draw_notify, args=(summary,body,dur)) 
#      t.start()        # Starts the thread 


def internet(url='http://www.google.com/'):
   import urllib.request
   try:
      urllib.request.urlopen(url, timeout=1)
      return True
   except urllib.request.URLError: return False

def get_public_IP(ntries=30):
   """
     Get Public IP. Max tries = ntries
   """
   if not internet(): return None
   def com():
      """ Aux func to choose random IP service """
      commands = ['wget -q -O - http://icanhazip.com/ | tail',
                  'wget -q -O - http://ip.42.pl/raw | tail',
                  'wget -q -O - http://ipecho.net/plain',
                  'wget -q -O - https://api.ipify.org']
      return choice(commands)
   correct = False
   cont = 0
   while not correct:
      try:
         command = com()  # Choose a random service
         IP = os.popen(command).read().rstrip().split()[0]
         nums = IP.split('.')
         aux = map(int,nums)
         correct = True
      except:
         correct = False
         sleep(randint(5,10))  # In case the web gets picky
      cont += 1
      if cont > ntries: return False
   return IP


def is_IP(ip):
   """
     Check if a string is formatted as a IPv4 IP address
     TODO: check also IPv6
   """
   try:
      aux = map(int,ip.split('.'))
      return True
   except:
      return False

def files(path='.',hidden=False,abspath=False):
   """
     Lists all the files in a folder.
       - hidden: list hidden files
       - abspath: return absolute paths
   """
   if path[-1] != '/': path += '/'
   if not os.path.isabs(path): path = os.path.abspath(path)
   else: pass   # Path is already absolute
   files = []
   #for f in os.walk(path).next()[2]:
   #TODO Recursive listing!!!
   for fs in os.walk(path):
      for f in fs[2]:
         if not hidden:
            if f[0] != '.':
               if abspath: files.append('/'.join([fs[0][0:-1],f]))
               else: files.append(f)
         else:
            if abspath:
               print('**','/'.join([fs[0][0:-1],f]))
               files.append('/'.join([fs[0][0:-1],f]))
            else: files.append(f)
   return files

def folders(path='.',hidden=False,abspath=False):
   """
     Lists all the subfolders in a folder.
       - hidden: list hidden folders
       - abspath: return absolute paths
   """
   if not os.path.isabs(path): path = os.path.abspath(path)
   else:
      if path[-1] == '/': path = path[0:-1] # Path is already absolute
   folders = []
   for f in os.walk(path).next()[1]:
      if not hidden:
         if f[0] != '.':
            if abspath: folders.append('/'.join([path,f]))
            else: folders.append(f)
      else:
         if abspath: folders.append('/'.join([path,f]))
         else: folders.append(f)
   return folders