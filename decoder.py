import os
import time
import sys
import platform
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--decode", help="Decode String", action="store_true")
parser.add_argument("-e", "--encode", help="Encode String", action="store_true")
parser.add_argument("-i", "--input", help="Input String")
parser.add_argument("-s", "--speed", help="Speed Set between 0.01 and 0.000001", type=float)
args = parser.parse_args()
if sys.platform == "win32":
    clear = 'cls'
elif sys.platform != "win32":
    clear = 'clear'
text = args.input
temp = ""
c = 0
try:
    for k in text:
        key = temp
        c += 1
        for i in range(25,3,-1):
            os.system(clear)
            if args.decode:
                temp = key + chr(ord(k)-i)
            elif args.encode:
                temp = key + chr(ord(k)+i)
            print("\n" + "   " + temp + text[c:])
            time.sleep(args.speed)
except:
    os.system(clear)
    print( "  Please use the following syntax: \n  python3 decoder.py -d -i string -s float \n  or \n  python3 decoder.py -e -i string -s float")
