import os
from lxml import etree
from lxml import objectify
import sys
import datetime

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
logPath = destPath + '\\ConvertSFELibsLog.txt'

print 'Decoded paths:'
print eagleLbrPath
print kicadLibPath
print kicadDcmPath
print logPath

# Open a log file, or create a new one
if os.path.isfile(logPath) == True:
	statinfo = os.stat(logPath)
	logFile = open(logPath, 'a')
	logFile.write('\n' + str(datetime.datetime.now()))
	logFile.write(" Appending log file\n")
else:
	print "creating log file"
	logFile = open(logPath, "w+")
	logFile.write('\n' + str(datetime.datetime.now()))
	logFile.write(" Created log file\n")

logFile.write( "eagleLbrPath: " + eagleLbrPath + '\n' )
logFile.write( "kicadLibPath: " + kicadLibPath + '\n' )
logFile.write( "kicadDcmPath: " + kicadDcmPath + '\n' )
logFile.write( "logPath: " + logPath + '\n' )

# Open the Eagle Library and objectify it
if os.path.isfile(eagleLbrPath) == True:
	statinfo = os.stat(eagleLbrPath)
	eagleLbrFile = open(eagleLbrPath, "r")
else:
	print "Invalid file name"
	
root = objectify.fromstring(eagleLbrFile.read(statinfo.st_size))

# Open the KiCad Library 
if os.path.isfile(kicadLibPath) == True:
	statinfo = os.stat(kicadLibPath)
	kicadLibFile = open(kicadLibPath, "a+")
	# Read the KiCad Library to memeory
	kicadLibMemory = kicadLibFile.read()
	#logFile.write(kicadLibMemory) # Enable this line to write memory to logfile
	#  ..Now kicadLibMemory is a string that is the input file
	kicadLibFile.close()
else:
	print "Invalid file name"

#Create DCM memory and give it a start line
kicadDcmMemory = 'EESchema-DOCLIB  Version 2.0\n'


print ""

tempName = ''
tempProdID = ''
tempDescription = ''

partsInspected = 0
validParts = 0
skippedParts = 0
notFoundInKicadLib = 0
dcmRecordsCreated = 0
prodIDFieldsAdded = 0
defaultProdIDsCreated = 0

logFile.write( "Starting to parse the eagle library\n" )

listNames = []
for i in range(0, MAX_EAGLE_PARTS):
	try:
		logFile.write("\n") #start with newline
		logFile.write( "Testing the devicset object\n" )
		root.drawing.library.devicesets.deviceset[i]
	except:
		logFile.write( "\ndeviceset exception occured\n" )
		break
	else:
		for j in range(0, MAX_EAGLE_PARTS):
			try:
				logFile.write("\n") #start with newline
				logFile.write( "Testing the subdevice object\n" )
				root.drawing.library.devicesets.deviceset[i].devices.device[j]
			except:
				logFile.write( "\nSub-device exception occured\n" )
				break
			else:
				try:
					logFile.write( "Attempting to get name... " )
					partsInspected = partsInspected + 1
					# Getting here means that a single valid device, or iterated device has been found
					
					#		Get the part name
					#       print ''.join(root.drawing.library.devicesets.deviceset[i].values()[0] + root.drawing.library.devicesets.deviceset[i].devices.device[j].values()[0])
					tempName = ''.join(root.drawing.library.devicesets.deviceset[i].values()[0] + root.drawing.library.devicesets.deviceset[i].devices.device[j].values()[0])
					# Do these conversions to be compatible with the kicad output script hackery
					tempName = tempName.replace("(", '_')
					tempName = tempName.replace(")", '_')
					tempName = tempName.replace("/", '_')
					tempName = tempName.replace(",", '_')
					logFile.write( "Name found, converted to: " + tempName + "\n")
					
					try:
						logFile.write( "Attempting to get the product id... " )
						#		Get the PROD_ID			
						tempProdID = ''.join(root.drawing.library.devicesets.deviceset[i].devices.device[j].technologies.technology.attribute.values()[1])
						logFile.write( "PROD_ID found: " + tempProdID + "\n")
					except:
						logFile.write( "PROD_ID not found, setting to XXX-00000\n")
						tempProdID = "XXX-00000"
						defaultProdIDsCreated = defaultProdIDsCreated + 1
						
					
					#		Get the description
					logFile.write( "Attempting to get the description... " )
					tempDescription = root.drawing.library.devicesets.deviceset[i].description.text
					tempDescription = ''.join([k if ord(k) != 181 else 'u' for k in tempDescription]) #replace mu symbol with u
					tempDescription = ''.join([k if ord(k) < 128 else ' ' for k in tempDescription]) #replace other non-ascii with space
					#logFile.write(str(i) + "." + str(j) + ": "	+ ''.join(tempDescription[:]) + '\n')
					tempDescription = tempDescription.replace("\n", '')
					tempDescription = tempDescription.replace("<h3>", '')
					tempDescription = tempDescription.replace("</h3>", ' ')
					tempDescription = tempDescription.replace("<p>", '')
					tempDescription = tempDescription.replace("</p>", ' ')
					tempDescription = tempDescription.replace("\n", '')
					logFile.write( "Description found: " + tempDescription[:30] + "(...)\n")
					
					#		Print what you know
					#print tempName, tempProdID#, tempDescription
					validParts = validParts + 1
					#print tempDescription
					
					#***********HERE IS WHERE THE WORK WOULD BE DONE*************
					# First, add the PROD_ID to the .lib file
					# Seek out the correct part
					#kicadLibFile.seek(0)
					#inputChar = kicadLibFile.read(1)
					#inputLine = []
					#while inputChar != '\n':
					#	inputChar = kicadLibFile.read(1)
					#	inputLine.extend(inputChar)
					#print ''.join(inputLine[:])
					findResults = kicadLibMemory.find(tempName, 0, len(kicadLibMemory))
					print findResults
					if findResults != -1:
						#Find the DEF tag and call that the parthead
						parthead = kicadLibMemory.find('DEF', findResults, len(kicadLibMemory))
						#Find the ENDDEF tag and call that the parttail
						parttail = kicadLibMemory.find('ENDDEF', findResults, len(kicadLibMemory))
						print parthead, parttail
						#Find the last "F" line
						fnum = 0
						locVar = kicadLibMemory.find('F' + str(fnum), parthead, parttail)
						while locVar != -1:
							fnum = fnum + 1
							locVar = kicadLibMemory.find('F' + str(fnum), parthead, parttail)
						#Check for valid
						if fnum != 0:
							fnum = fnum - 1
							locVar = kicadLibMemory.find('F' + str(fnum), parthead, parttail)
							#Now points to last F number
							#Go to end line
							locVar = kicadLibMemory.find('\n', locVar, parttail)
							locVar = locVar + 1
							insertPhrase = 'F' + str(fnum + 1) + ' "' + str(tempProdID) + '" 160 215 60 H V C CNN "PROD_ID"\n'
							kicadLibMemory = kicadLibMemory[:locVar] + insertPhrase + kicadLibMemory[locVar:]
							prodIDFieldsAdded = prodIDFieldsAdded + 1
					else:
						notFoundInKicadLib = notFoundInKicadLib + 1
					#Now write a description
					
					kicadDcmMemory = kicadDcmMemory[:] + '#\n$CMP ' + tempName + '\nD ' + tempDescription + '\nK PROD_ID:' + tempProdID + '\n$ENDCMP\n'
					dcmRecordsCreated = dcmRecordsCreated + 1
				except:
					skippedParts = skippedParts + 1
					print "\nSkipped a part\n"
					logFile.write( "\nParsing exception occured\n" )
					print tempDescription
					break

print ""
print "Number of parts inspected: ", partsInspected
print "Number of valid parts found: ", validParts
print "Number of parts skipped: ", skippedParts
print "Number not found in KiCad libs: ", notFoundInKicadLib
print "Number of DCM entries created: ", dcmRecordsCreated
print "Number PROD_ID fields created: ", prodIDFieldsAdded
print "Default PROD_ID used: ", defaultProdIDsCreated
print ""

logFile.write( "Number of parts inspected: " + str(partsInspected) + '\n' )
logFile.write( "Number of valid parts found: " + str(validParts) + '\n' )
logFile.write( "Number of parts skipped: " + str(skippedParts) + '\n' )
logFile.write( "Number not found in KiCad libs: " + str(notFoundInKicadLib) + '\n' )
logFile.write( "Number of DCM entries created: " + str(dcmRecordsCreated) + '\n' )
logFile.write( "Number PROD_ID fields created: " + str(prodIDFieldsAdded) + '\n' )
logFile.write( "Default PROD_ID used: " + str(defaultProdIDsCreated) + '\n' )

eagleLbrFile.close()

#logFile.write(kicadLibMemory) # Enable this line to write memory to logfile
logFile.write(str(datetime.datetime.now()) + ' ' )
logFile.write("Closing log file\n\n\n\n")
logFile.close()

# Write out the kicadLibMemory
if os.path.isfile(kicadLibPath) == True:
	statinfo = os.stat(kicadLibPath)
	kicadLibFile = open(kicadLibPath, "w+")
	# Read the KiCad Library to memeory
	kicadLibFile.write(kicadLibMemory) # Enable this line to write memory to OUTPUT
	kicadLibFile.close()
else:
	print "Invalid file name"

# Write out the kicadDcmMemory (Trash the existing file)
#       OLD WAY:
#if os.path.isfile(kicadDcmPath) == True:
#	statinfo = os.stat(kicadDcmPath)
#	kicadDcmFile = open(kicadDcmPath, "w+")
#	# Read the KiCad Library to memeory
#else:
#	print "Invalid file name"

if os.path.isfile(kicadDcmPath) == True:
	statinfo = os.stat(kicadDcmPath)
	kicadDcmFile = open(kicadDcmPath, 'a')
else:
	print "creating dcm file"
	kicadDcmFile = open(kicadDcmPath, "w+")
kicadDcmFile.write(kicadDcmMemory) # Enable this line to write memory to OUTPUT
kicadDcmFile.close()
	
	
print "File IO complete"




#Note: DCM format:

#		EESchema-DOCLIB  Version 2.0
#		#
#		$CMP 0.18UF-0603-10V-10%
#		D Description line goes here
#		K Term1 Term2 PROD_ID:xxx-00000
#		$ENDCMP
#		#
#		#End Doc Library