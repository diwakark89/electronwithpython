#!/usr/bin/python
from pip._vendor.distlib.compat import raw_input


fo=open("test.txt", "r+")
for x in fo :
    print(x)
fo.close()