#!/usr/bin/python
#-*- encoding:utf-8 -*-
import os
import sys
import random
from zipfile import ZipFile
arg=sys.argv[1]
passlen=input("Length of password:")
password=""
charset="0123456789qwertyuıopğüasdfghjklşizxcvbnmöçQWERTYUIOPĞÜASDFGHJKLŞİZXCVBNMÖÇ"
# while True:
#     for i in range(0,passlen):
#         password+=charset[random.randint(0,73)]
#     if len(os.popen("unzip -p -P %s %s" %(password,arg)).read().split()) == 0:
#         password=""
#         pass
#     else:
#         print "Password found:",password,os.popen("unzip -p -P %s %s" %(password,arg)).read().split()
#        exit()
while True:
    for i in range(0,passlen):
        password+=charset[random.randint(0,73)]
    try:
        with ZipFile(arg) as zf:
            zf.extractall(pwd=password)
        print "Password found:",password
        break
        exit()
    except:
        password=""
        pass
