import os
from lxml import etree
from lxml import objectify
import sys

MAX_EAGLE_PARTS = 1000

print"" # print a new line

# C:\github\SparkFun-Eagle-Libraries C:\github\SparkFun-KiCad-Libraries\Conversion\TestLibs SparkFun-Capacitors
numArgs = len(sys.argv)
if numArgs < 4:
	#Print help
	print "Not enough arguments"
	print "Requires: <source path> <dest path> <library name>"
	print "Example: Python file.py C:\github\SparkFun-Eagle-Libraries C:\github\SparkFun-KiCad-Libraries\Conversion\TestLibs SparkFun-Capacitors"
	exit()

sourcePath = sys.argv[1]
destPath = sys.argv[2]
commonName = sys.argv[3]

eagleLbrPath = sourcePath + '\\' + commonName + '.lbr'
kicadLibPath = destPath + '\\' + commonName + '.lib'
kicadDcmPath = destPath + '\\' + commonName + '.dcm'

print 'Decoded paths:'
print eagleLbrPath
print kicadLibPath
print kicadDcmPath
