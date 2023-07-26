import os
from lxml import etree
from lxml import objectify
import sys

MAX_EAGLE_PARTS = 1000

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

#print root.drawing.library.devicesets.deviceset[0].description.text

#print root.drawing.library.devicesets.deviceset[0].devices.device.technologies.technology.attribute.values()
#print root.drawing.library.devicesets.deviceset[0].devices.device.technologies.technology.attrib[1]
#print root.drawing.library.devicesets.deviceset[0].devices.device.technologies.technology.attrib[2]

print ""

listTemp = []

# make list of "name" and "Prod ID" and full descriptions
listNames = []
for i in range(0, MAX_EAGLE_PARTS):
	try:
		root.drawing.library.devicesets.deviceset[i]
	except:
		break
	else:
		#print root.drawing.library.devicesets.deviceset[i].attrib
		del listTemp[:]
		listTemp.extend(root.drawing.library.devicesets.deviceset[i].values())
		if len(listTemp) > 0:
			listNames.extend(" ")
			listNames[len(listNames) - 1] = listTemp[0]
		##print root.drawing.library.devicesets.deviceset[i].devices.device.technologies.technology.attribute.attrib


listProdIDs = []
for i in range(0, MAX_EAGLE_PARTS):
	try:
		root.drawing.library.devicesets.deviceset[i]
	except:
		break
	else:
		#print root.drawing.library.devicesets.deviceset[i].devices.device.technologies.technology.attribute.values()
		del listTemp[:]
		listTemp.extend(root.drawing.library.devicesets.deviceset[i].devices.device.technologies.technology.attribute.values())
		if len(listTemp) > 0:
			listProdIDs.extend(" ")
			listProdIDs[len(listProdIDs) - 1] = listTemp[1]
		#print root.drawing.library.devicesets.deviceset[i].devices.device.technologies.technology.attribute.attrib

listDescriptions = []
for i in range(0, MAX_EAGLE_PARTS):
	try:
		root.drawing.library.devicesets.deviceset[i]
	except:
		break
	else:
		#print root.drawing.library.devicesets.deviceset[i].devices.device.technologies.technology.attribute.values()
		del listTemp[:]
		listTemp.extend(root.drawing.library.devicesets.deviceset[i].description.text)
		if len(listTemp) > 0:
			listDescriptions.extend(" ")
			listDescriptions[len(listDescriptions) - 1] = ''.join(listTemp[:])
		#print root.drawing.library.devicesets.deviceset[i].devices.device.technologies.technology.attribute.attrib
# Report list lengths
print "Part names found: ", len(listNames)
print "Part IDs found: ", len(listProdIDs)
print "Descriptions found: ", len(listDescriptions)
print ""

for i in range(0, MAX_EAGLE_PARTS):
	if i < len(listNames) and i < len(listProdIDs) and i < len(listDescriptions):
		print listNames[i], "\n", listProdIDs[i], "\n", listDescriptions[i], "\n\n"

# print the lists
##print listNames
#print root.drawing.library.devicesets.deviceset[3].description.text

myFile.close()
print "File IO complete"

