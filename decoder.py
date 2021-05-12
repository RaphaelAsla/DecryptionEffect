import os
from time import sleep
text = input()
temp = ""
c = 0
for k in text:
    key = temp 
    c += 1
    for i in range(25,3,-1):   
        os.system('cls') 
        temp = key + chr(ord(k)-i)
        print(temp + text[c:])
        sleep(0.0001)
