import os
import sys
import datetime

MAX_EAGLE_PARTS = 1000

print"" # print a new line

# C:\github\SparkFun-Eagle-Libraries C:\github\SparkFun-KiCad-Libraries\Conversion\TestLibs SparkFun-Capacitors
numArgs = len(sys.argv)
if numArgs < 4:
	#Print help
	print "Not enough arguments"
	print "Requires: <source path> <dest path> <mod name>"
	print "Example: Python file.py C:\github\SparkFun-KiCad-Libraries\SparkFun.pretty C:\github\SparkFun-KiCad-Libraries\Export.pretty SFE_LOGO_FLAME_.2"
	exit()

sourcePath = sys.argv[1]
destPath = sys.argv[2]
commonName = sys.argv[3]

modLinePath = sourcePath + '\\' + commonName + '.kicad_mod'
modPolyPath = destPath + '\\' + commonName + '.kicad_mod'
logPath = destPath + '\\scriptOutputLog.txt'

print 'Decoded paths:'
print modLinePath
print modPolyPath
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

logFile.write( "modLinePath: " + modLinePath + '\n' )
logFile.write( "modPolyPath: " + modPolyPath + '\n' )
logFile.write( "logPath: " + logPath + '\n' )

# Open the export mod style file
if os.path.isfile(modLinePath) == True:
	statinfo = os.stat(modLinePath)
	modLineFile = open(modLinePath, "r")
	# Read the KiCad Library to memeory
	kicadLineModMemory = modLineFile.read()
	#  ..Now kicadLibMemory is a string that is the input file
	modLineFile.close()
else:
	print "Invalid file name"


#Create the output file memory
kicadPolyModMemory = ''#start with blank file


print ""


logFile.write( "Starting to parse input mod file\n" )

#First, seek out initial "fp_line" text -- copy all lines before the line with it.
locVar = kicadLineModMemory.find("fp_line", 0, len(kicadLineModMemory)) - 3
kicadPolyModMemory = kicadPolyModMemory + kicadLineModMemory[:locVar]

#Second, capture the layer real quick for later
layerDefStart = kicadLineModMemory.find("(layer", locVar, len(kicadLineModMemory))
layerDefEnd = kicadLineModMemory.find(")", layerDefStart, len(kicadLineModMemory)) + 1

#Now we want to do the following type format
	#  (fp_poly (pts
	#   (xy 0.982653 -2.516805)
	#	(xy 1.161515 -2.508866)
kicadPolyModMemory = kicadPolyModMemory + "(fp_poly (pts\n"

#But an input line looks like:
	#  (fp_line (start 4.6482 -6.53796) (end 4.6482 -6.51764) (layer F.SilkS) (width 0.00762))
#... and all we need is the first point from it.
#Find "(fp_line (start " statments until there are none
exitCondition = 0
while exitCondition == 0:
	locVar = kicadLineModMemory.find("(fp_line (start ", locVar, len(kicadLineModMemory))
	if locVar == -1:
		exitCondition = 1
	else:
		# move to data
		print( str(locVar) )
		locVar = locVar + 16
		dataStart = locVar
		dataEnd = kicadLineModMemory.find(")", dataStart, len(kicadLineModMemory))
		#Create the point in file
		kicadPolyModMemory = kicadPolyModMemory + "    (xy " + kicadLineModMemory[dataStart:dataEnd] + ")\n"

# Now finish the file
#    (xy 15.279895 -0.93621)) (layer F.SilkS) (width 0.01))
#)

kicadPolyModMemory = kicadPolyModMemory + ") " + kicadLineModMemory[layerDefStart:layerDefEnd] + " (width 0.01))\n"
kicadPolyModMemory = kicadPolyModMemory + ")\n"

#print ""
#print "Number of parts inspected: ", partsInspected
#print "Number of valid parts found: ", validParts
#print "Number of parts skipped: ", skippedParts
#print "Number not found in KiCad libs: ", notFoundInKicadLib
#print "Number of DCM entries created: ", dcmRecordsCreated
#print "Number PROD_ID fields created: ", prodIDFieldsAdded
#print "Default PROD_ID used: ", defaultProdIDsCreated
#print ""
#
#logFile.write( "Number of parts inspected: " + str(partsInspected) + '\n' )
#logFile.write( "Number of valid parts found: " + str(validParts) + '\n' )
#logFile.write( "Number of parts skipped: " + str(skippedParts) + '\n' )
#logFile.write( "Number not found in KiCad libs: " + str(notFoundInKicadLib) + '\n' )
#logFile.write( "Number of DCM entries created: " + str(dcmRecordsCreated) + '\n' )
#logFile.write( "Number PROD_ID fields created: " + str(prodIDFieldsAdded) + '\n' )
#logFile.write( "Default PROD_ID used: " + str(defaultProdIDsCreated) + '\n' )

#eagleLbrFile.close()

#logFile.write(kicadLibMemory) # Enable this line to write memory to logfile
logFile.write(str(datetime.datetime.now()) + ' ' )
logFile.write("Closing log file\n\n\n\n")
logFile.close()

# Write out the kicadPolyModMemory
if os.path.isfile(modPolyPath) == True:
	statinfo = os.stat(modPolyPath)
	modPolyFile = open(modPolyPath, "w+")
	# Read the KiCad Library to memeory
else:
	print "creating poly .kicad_mod file"
	modPolyFile = open(modPolyPath, "w+")
modPolyFile.write(kicadPolyModMemory) # Enable this line to write memory to OUTPUT
modPolyFile.close()

	
print "File IO complete"
