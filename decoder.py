import os
import time
import sys
import platform
if sys.platform == "win32":
    clear = 'cls'
elif sys.platform != "win32":
    clear = 'clear'
text = "lxxt>33mqtvsgshiv2oette"
temp = ""
c = 0
for k in text:
    key = temp
    c += 1
    for i in range(20,3,-1):
        os.system(clear)
        temp = key + chr(ord(k)-i)
        print(temp + text[c:])
        time.sleep(0.01)
