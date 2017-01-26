import os
from lxml import etree
from lxml import objectify
import sys

print"" # print a new line

numArgs = len(sys.argv)
if numArgs < 2:
	#Print help
	print "Not enough arguments"
	print "Example: Python file.py C:\github\SparkFun-Eagle-Libraries\SparkFun-IC-Conversion.lbr"
	exit()

myFileName = sys.argv[1]

if os.path.isfile(myFileName) == True:
	statinfo = os.stat(myFileName)
	myFile = open(myFileName, "r")
else:
	print "Invalid file name"
	exit()
	
	#print myFile.read(statinfo.st_size)

#root = objectify.parse(myFileName)
root = objectify.fromstring(myFile.read(statinfo.st_size))
#print(etree.tostring(root, pretty_print=True))

print root.drawing.library.devicesets.deviceset[0].description.text

print root.drawing.library.devicesets.deviceset[0].devices.device.technologies.technology.attribute.attrib
#print root.drawing.library.devicesets.deviceset[0].devices.device.technologies.technology.attrib[1]
#print root.drawing.library.devicesets.deviceset[0].devices.device.technologies.technology.attrib[2]

print ""
for i in range(0, 100):
	try: root.drawing.library.devicesets.deviceset[i]
	except: break
	print root.drawing.library.devicesets.deviceset[i].attrib

myFile.close()
print "File IO complete"

