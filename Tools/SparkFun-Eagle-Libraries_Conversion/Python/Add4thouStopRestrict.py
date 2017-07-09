import os
import sys
import datetime

def ensure_dir(file_path):
	try: 
		os.makedirs(file_path)
	except OSError:
		if not os.path.isdir(file_path):
			raise
		
MAX_EAGLE_PARTS = 1000

print "" # print a new line

numArgs = len(sys.argv)
if numArgs < 4:
	#Print help
	print "Not enough arguments"
	print "Requires: <source path> <dest path> <inchs of clearance>"
	print "Example: python Add4thouSilkRestrict.py E:\github\SparkFun-KiCad-Libraries\Footprints E:\github\SparkFun-KiCad-Libraries\Tools\SparkFun-Eagle-Libraries_Conversion\temp 0.004"
	exit()

sourcePath = sys.argv[1]
destPath = sys.argv[2]
clearance = "{:6.4f}".format(float(sys.argv[3]) * 25.4)

directoryList = []
for dirname in os.listdir(sourcePath):
##Save directory listing
#	directoryList.append(filename)
#print directoryList

	for filename in os.listdir(sourcePath + "\\" + dirname):
		ensure_dir(destPath + "\\" + dirname)
		print "Opening",
		fullFilePath = sourcePath + "\\" + dirname + "\\" + filename
		print fullFilePath
		# Open the export mod style file
		if os.path.isfile(fullFilePath) == True:
			statinfo = os.stat(fullFilePath)
			workingFileHandle = open(fullFilePath, "r")
			# Read the footprint to memeory
			workingFileMemory = workingFileHandle.read()
			#  ..Now workingFileMemory is a string that is the input file
			
			
			#First, seek out initial "fp_line" text -- copy all lines before the line with it.
			locVar = workingFileMemory.find("(pad ", 0, len(workingFileMemory))
			if locVar > 0:
				#This file has one or more
				fileVar = 0
				parsingFile = 1
				while parsingFile == 1 and fileVar < len(workingFileMemory):
					locVar = workingFileMemory.find("(pad ", fileVar, len(workingFileMemory))
					if locVar > 0:
						print "Found pad!",
						fileVar = locVar + 1
						leftParen = locVar
						leftParenCount = 1
						rightParenCount = 0
						countIsNonZero = 1
						nextParen = leftParen
						while countIsNonZero == 1:
							
							#Find next paren
							var2 = workingFileMemory.find("(", nextParen + 1, len(workingFileMemory))
							var1 = workingFileMemory.find(")", nextParen + 1, len(workingFileMemory))
							if var1 != -1 or var2 != 0:
								if var2 < var1 and var2 > 0:
									#set output = var2
									nextParen = var2
								else:
									nextParen = var1
								#Found something
								#modify counts
								if workingFileMemory[nextParen] == '(':
									#print workingFileMemory[nextParen]
									leftParenCount = leftParenCount + 1
								elif workingFileMemory[nextParen] == ')':
									#print workingFileMemory[nextParen]
									rightParenCount = rightParenCount + 1
							else:
								print "No more chars"
								countIsNonZero = 0
							#print leftParenCount,
							#print ",",
							#print rightParenCount
							#if counts are equal, do a thing then bail
							if leftParenCount == rightParenCount:
								countIsNonZero = 0
								rightParen = nextParen + 1
								print "Syntax Correct!"
								print workingFileMemory[leftParen:rightParen]
								#Look for existing parameter
								var1 = workingFileMemory.find("solder_mask_margin", leftParen, rightParen)
								if var1 != -1:
									#delete it
									var2 = workingFileMemory.find(")", var1, rightParen)
									tempFileMemory = workingFileMemory[:var1-2] + workingFileMemory[var2+1:]
									#Calculate the number of chars removed
									removedChars = var2 - var1 + 3
									#offset rightParen
									rightParen = rightParen - removedChars
									workingFileMemory = tempFileMemory
								#Now write the new value
								tempFileMemory = workingFileMemory[:rightParen-1] + " (solder_mask_margin " + clearance + ")" + workingFileMemory[rightParen-1:]
								workingFileMemory = tempFileMemory
								
					else:
						parsingFile = 0
				print workingFileMemory[locVar-3:locVar+3]
			else:
				#This file has none!
				print "File has no pads!"

			#print tempFileMemory
			#programPause = raw_input("Press the <ENTER> key to continue...")

			#Write the output file
			outputFilePath = destPath + "\\" + dirname + "\\" + filename
			# Write out the workingFileMemory
			if os.path.isfile(outputFilePath) == True:
				statinfo = os.stat(outputFilePath)
				outputFileHandle = open(outputFilePath, "w+")
				# Read the KiCad Library to memeory
			else:
				print "creating poly .kicad_mod file"
				outputFileHandle = open(outputFilePath, "w+")
			outputFileHandle.write(workingFileMemory) # Enable this line to write memory to OUTPUT
			outputFileHandle.close()
			
			workingFileHandle.close()
		else:
			print "File not opened!"

		print ""

		#Create the output file memory
		outputMemory = ''#start with blank file
	

#modLinePath = sourcePath + '\\' + commonName + '.kicad_mod'
#modPolyPath = destPath + '\\' + commonName + '.kicad_mod'
#logPath = destPath + '\\scriptOutputLog.txt'
#
#print 'Decoded paths:'
#print modLinePath
#print modPolyPath
#print logPath
#
## Open a log file, or create a new one
#if os.path.isfile(logPath) == True:
#	statinfo = os.stat(logPath)
#	logFile = open(logPath, 'a')
#	logFile.write('\n' + str(datetime.datetime.now()))
#	logFile.write(" Appending log file\n")
#else:
#	print "creating log file"
#	logFile = open(logPath, "w+")
#	logFile.write('\n' + str(datetime.datetime.now()))
#	logFile.write(" Created log file\n")
#
#logFile.write( "modLinePath: " + modLinePath + '\n' )
#logFile.write( "modPolyPath: " + modPolyPath + '\n' )
#logFile.write( "logPath: " + logPath + '\n' )
#
## Open the export mod style file
#if os.path.isfile(modLinePath) == True:
#	statinfo = os.stat(modLinePath)
#	modLineFile = open(modLinePath, "r")
#	# Read the KiCad Library to memeory
#	kicadLineModMemory = modLineFile.read()
#	#  ..Now kicadLibMemory is a string that is the input file
#	modLineFile.close()
#else:
#	print "Invalid file name"
#
#
##Create the output file memory
#kicadPolyModMemory = ''#start with blank file
#
#
#print ""
#
#
#logFile.write( "Starting to parse input mod file\n" )
#
##First, seek out initial "fp_line" text -- copy all lines before the line with it.
#locVar = kicadLineModMemory.find("fp_line", 0, len(kicadLineModMemory)) - 3
#kicadPolyModMemory = kicadPolyModMemory + kicadLineModMemory[:locVar]
#
##Second, capture the layer real quick for later
#layerDefStart = kicadLineModMemory.find("(layer", locVar, len(kicadLineModMemory))
#layerDefEnd = kicadLineModMemory.find(")", layerDefStart, len(kicadLineModMemory)) + 1
#
##Now we want to do the following type format
#	#  (fp_poly (pts
#	#   (xy 0.982653 -2.516805)
#	#	(xy 1.161515 -2.508866)
#kicadPolyModMemory = kicadPolyModMemory + "(fp_poly (pts\n"
#
##But an input line looks like:
#	#  (fp_line (start 4.6482 -6.53796) (end 4.6482 -6.51764) (layer F.SilkS) (width 0.00762))
##... and all we need is the first point from it.
##Find "(fp_line (start " statments until there are none
#exitCondition = 0
#while exitCondition == 0:
#	locVar = kicadLineModMemory.find("(fp_line (start ", locVar, len(kicadLineModMemory))
#	if locVar == -1:
#		exitCondition = 1
#	else:
#		# move to data
#		print( str(locVar) )
#		locVar = locVar + 16
#		dataStart = locVar
#		dataEnd = kicadLineModMemory.find(")", dataStart, len(kicadLineModMemory))
#		#Create the point in file
#		kicadPolyModMemory = kicadPolyModMemory + "    (xy " + kicadLineModMemory[dataStart:dataEnd] + ")\n"
#
## Now finish the file
##    (xy 15.279895 -0.93621)) (layer F.SilkS) (width 0.01))
##)
#
#kicadPolyModMemory = kicadPolyModMemory + ") " + kicadLineModMemory[layerDefStart:layerDefEnd] + " (width 0.01))\n"
#kicadPolyModMemory = kicadPolyModMemory + ")\n"
#
##print ""
##print "Number of parts inspected: ", partsInspected
##print "Number of valid parts found: ", validParts
##print "Number of parts skipped: ", skippedParts
##print "Number not found in KiCad libs: ", notFoundInKicadLib
##print "Number of DCM entries created: ", dcmRecordsCreated
##print "Number PROD_ID fields created: ", prodIDFieldsAdded
##print "Default PROD_ID used: ", defaultProdIDsCreated
##print ""
##
##logFile.write( "Number of parts inspected: " + str(partsInspected) + '\n' )
##logFile.write( "Number of valid parts found: " + str(validParts) + '\n' )
##logFile.write( "Number of parts skipped: " + str(skippedParts) + '\n' )
##logFile.write( "Number not found in KiCad libs: " + str(notFoundInKicadLib) + '\n' )
##logFile.write( "Number of DCM entries created: " + str(dcmRecordsCreated) + '\n' )
##logFile.write( "Number PROD_ID fields created: " + str(prodIDFieldsAdded) + '\n' )
##logFile.write( "Default PROD_ID used: " + str(defaultProdIDsCreated) + '\n' )
#
##eagleLbrFile.close()
#
##logFile.write(kicadLibMemory) # Enable this line to write memory to logfile
#logFile.write(str(datetime.datetime.now()) + ' ' )
#logFile.write("Closing log file\n\n\n\n")
#logFile.close()
#
## Write out the kicadPolyModMemory
#if os.path.isfile(modPolyPath) == True:
#	statinfo = os.stat(modPolyPath)
#	modPolyFile = open(modPolyPath, "w+")
#	# Read the KiCad Library to memeory
#else:
#	print "creating poly .kicad_mod file"
#	modPolyFile = open(modPolyPath, "w+")
#modPolyFile.write(kicadPolyModMemory) # Enable this line to write memory to OUTPUT
#modPolyFile.close()

	
print "Script complete"

