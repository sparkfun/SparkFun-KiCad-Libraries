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

tempName = ''
tempProdID = ''
tempDescription = ''

partsInspected = 0
validParts = 0
skippedParts = 0

listNames = []
for i in range(0, MAX_EAGLE_PARTS):
	try:
		root.drawing.library.devicesets.deviceset[i]
	except:
		break
	else:
		for j in range(0, MAX_EAGLE_PARTS):
			try:
				root.drawing.library.devicesets.deviceset[i].devices.device[j]
			except:
				break
			else:
				try:
					partsInspected = partsInspected + 1
					# Getting here means that a single valid device, or iterated device has been found
					
					#		Get the part name
					#       print ''.join(root.drawing.library.devicesets.deviceset[i].values()[0] + root.drawing.library.devicesets.deviceset[i].devices.device[j].values()[0])
					tempName = ''.join(root.drawing.library.devicesets.deviceset[i].values()[0] + root.drawing.library.devicesets.deviceset[i].devices.device[j].values()[0])

					#		Get the PROD_ID			
					tempProdID = ''.join(root.drawing.library.devicesets.deviceset[i].devices.device[j].technologies.technology.attribute.values()[1])
					
					#		Get the description
					tempDescription = root.drawing.library.devicesets.deviceset[i].description.text
					tempDescription = tempDescription.replace("\n", '')
					tempDescription = tempDescription.replace("<h3>", '')
					tempDescription = tempDescription.replace("</h3>", ' ')
					tempDescription = tempDescription.replace("<p>", '')
					tempDescription = tempDescription.replace("</p>", ' ')
					tempDescription = tempDescription.replace("\n", '')
					
					#		Print what you know
					print tempName, tempProdID, tempDescription
					validParts = validParts + 1
					
					#***********HERE IS WHERE THE WORK WOULD BE DONE*************
				except:
					skippedParts = skippedParts + 1
					print "\nSkipped a part\n"
					break

print ""
print "Number of parts inspected: ", partsInspected
print "Number of valid parts found: ", validParts
print "Number of parts skipped: ", skippedParts
print ""

myFile.close()
print "File IO complete"

