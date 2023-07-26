import os
import sys
import datetime

print "" # print a new line
print "Running KiCadPadMod.py"

def ensure_dir(file_path):
	try: 
		os.makedirs(file_path)
	except OSError:
		if not os.path.isdir(file_path):
			raise

numArgs = len(sys.argv)
lastArg = numArgs - 1
#if numArgs < 3:
#	#Print help
#	print ""
#	print "Not enough arguments!"
#	print "See /Documentation/KiCadPadMod.md for manual."
#	exit()

#Iterate through the line and inspect all the elements.
argPointer = 1
notEnoughArgs = 0
justListArgs = 0

subArgString = "undef"
padArgString = "undef"
nopadArgString = "undef"
onlypadArgString = "undef"
addArgString = "undef"
remArgString = "undef"
modArgString = "undef"
modArgValueString = "undef"
modArgValueMMString = "undef"
sourcePath = "undef"
destPath = "undef"
searchTermString = "undef"

#Insert the following to debug parsing
#print "   Result..."
#print "     currentArg =",
#print sys.argv[argPointer]
#print "     argPointer =",
#print argPointer
#print "     lastArg =",
#print lastArg

if lastArg < 3:  #At min, we need .py path path
	notEnoughArgs = 1

#Look for -l
if sys.argv[argPointer] == "-l" and notEnoughArgs == 0 :
	justListArgs = 1
#	print "-l option in effect, not touching files"
	if argPointer <= lastArg - 2:
		argPointer += 1
	else:
		notEnoughArgs = 1

#look for sub
if sys.argv[argPointer] == "-sub" and notEnoughArgs == 0 :
#	print "we have sub, need 3 additional args"
	if argPointer <= lastArg - 3:
		argPointer += 1
		subArgString = sys.argv[argPointer]
		argPointer += 1
	else:
		notEnoughArgs = 1

#look for pad
if sys.argv[argPointer] == "-pad" and notEnoughArgs == 0 :
#	print "we have pad, need 3 additional args"
	if argPointer <= lastArg - 3:
		argPointer += 1
		padArgString = sys.argv[argPointer]
		argPointer += 1
	else:
		notEnoughArgs = 1

#look for nopad
if sys.argv[argPointer] == "-nopad" and notEnoughArgs == 0 :
#	print "we have nopad, need 3 additional args"
	if argPointer <= lastArg - 3:
		argPointer += 1
		nopadArgString = sys.argv[argPointer]
		argPointer += 1
	else:
		notEnoughArgs = 1

#look for onlypad
if sys.argv[argPointer] == "-onlypad" and notEnoughArgs == 0 :
#	print "we have onlypad, need 3 additional args"
	if argPointer <= lastArg - 3:
		argPointer += 1
		onlypadArgString = sys.argv[argPointer]
		argPointer += 1
	else:
		notEnoughArgs = 1

#look for add
if sys.argv[argPointer] == "-add" and notEnoughArgs == 0 :
#	print "we have add, need 3 additional args"
	if argPointer <= lastArg - 3:
		argPointer += 1
		addArgString = sys.argv[argPointer]
		argPointer += 1
	else:
		notEnoughArgs = 1

#look for rem
if sys.argv[argPointer] == "-rem" and notEnoughArgs == 0 :
#	print "we have rem, need 3 additional args"
	if argPointer <= lastArg - 3:
		argPointer += 1
		remArgString = sys.argv[argPointer]
		argPointer += 1
	else:
		notEnoughArgs = 1

#look for mod
if sys.argv[argPointer] == "-mod" and notEnoughArgs == 0 :
#	print "we have mod, need 4 additional args"
	if argPointer <= lastArg - 4:
		argPointer += 1
		modArgString = sys.argv[argPointer]
		argPointer += 1
		modArgValueString = sys.argv[argPointer]
		modArgValueMMString = "{:6.4f}".format(float(sys.argv[argPointer]) * 25.4)
		argPointer += 1
	else:
		notEnoughArgs = 1

#Now there should be two args remaining
sourcePath = sys.argv[argPointer]
argPointer += 1
destPath = sys.argv[argPointer]
argPointer += 1

#If there is another term, it's the search term
if argPointer <= lastArg:
	searchTermString = sys.argv[argPointer]

if justListArgs == 1 or notEnoughArgs == 1:
	print ""
	if justListArgs == 1:
		print "-l option in effect, listing results"
		if notEnoughArgs == 1:
			print " (Notice: parsing failed)"
	else:
		print "-l option not in effect, but parsing failed so listing results anyhow"
	print ""
	print "subArgString:",
	print subArgString
	print "padArgString:",
	print padArgString
	print "nopadArgString:",
	print nopadArgString
	print "onlypadArgString:",
	print onlypadArgString
	print "addArgString:",
	print addArgString
	print "remArgString:",
	print remArgString
	print "modArgString:",
	print modArgString
	print "modArgValueString:",
	print modArgValueString
	print "modArgValueMMString:",
	print modArgValueMMString
	print "sourcePath:",
	print sourcePath
	print "destPath:",
	print destPath
	print "searchTermString:",
	print searchTermString

# Now check for valid options
invalidOptions = 0
optionsCount = 0

print ""
if subArgString != "undef":
	if subArgString == "0" or subArgString == "1":
		print "Valid sublevel"
	else:
		invalidOptions = 1
		print "[ERROR] Invalid sublevel option"
else:
	print "No sublevel specified, operation TBD"
	
if padArgString != "undef":
	if padArgString == "SMD" or padArgString == "PTH" or padArgString == "NPTH":
		print "Valid pad value"
	else:
		invalidOptions = 1
		print "[ERROR] Invalid pad option"
else:
	invalidOptions = 1
	print "no pad option specified!"

if nopadArgString != "undef":
	if nopadArgString == "CENTER":
		print "excluding center pad"
	else:
		invalidOptions = 1
		print "[ERROR] Invalid nopad option"
else:
	print "nopad not used, including center pad."

if onlypadArgString != "undef":
	if onlypadArgString == "CENTER":
		print "Only operation on center pad"
	else:
		invalidOptions = 1
		print "[ERROR] Invalid onlypad option"
else:
	print "onlypad not used, including all pads."

if nopadArgString != "undef" and onlypadArgString != "undef":
	invalidOptions = 1
	print "[ERROR] You can't exclude the center pad but only operate on it!"

if addArgString != "undef":
	if addArgString == "F.Paste" or addArgString == "B.Paste" or addArgString == "F.Mask" or addArgString == "B.Mask":
		print "Valid add value"
		optionsCount += 1
	else:
		invalidOptions = 1
		print "[ERROR] Invalid add option"
else:
	print "No add option specified."

if remArgString != "undef":
	if remArgString == "F.Paste" or remArgString == "B.Paste" or remArgString == "F.Mask" or remArgString == "B.Mask":
		print "Valid rem value"
		optionsCount += 1
	else:
		invalidOptions = 1
		print "[ERROR] Invalid rem option"
else:
	print "No rem option specified."

if modArgString != "undef":
	if modArgString == "PadClearance" or modArgString == "MaskClearance" or modArgString == "PasteClearance":
		print "Valid mod value"
		optionsCount += 1
	else:
		invalidOptions = 1
		print "[ERROR] Invalid mod option"
else:
	print "No mod option specified."

if optionsCount == 0:
	invalidOptions = 1
	print "[ERROR] No operations specified."

if optionsCount > 1:
	invalidOptions = 1
	print "[ERROR] More than one option specified."
	print "  (Use batch file to run script multiple times instead.)"

# Now check for valid paths
if sourcePath != "undef":
	print "Source path specified",
else:
	invalidOptions = 1
	print "[ERROR] Source path not present"

if destPath != "undef":
	print "Destination path specified",
else:
	invalidOptions = 1
	print "[ERROR] Destination path not present"

if searchTermString != "undef":
	print "Search terms specified",
else:
	print "No search terms provided, using *.kicad_mod"
	
if justListArgs == 1 or notEnoughArgs == 1  or invalidOptions == 1:
	print ""
	if notEnoughArgs == 1:
		print "[ERROR] Encountered invalid syntax."
	if invalidOptions == 1:
		print "[ERROR] Encountered invalid options."
	if justListArgs == 1 and notEnoughArgs == 0  and invalidOptions == 0:
		print "Syntax and parsing passed!"
	else:
		exit()
else:
	print ""
	print "Option parsing passed!"

# Now check file paths are actually valid
pathError = 0

print ""
print "Checking file paths"

print "Destination path:",
print destPath
if not os.path.isdir(destPath):
	print "   Destination path does not exists.  Will be created!"
else:
	print "   Destination path exists!"

print "Source path:",
print sourcePath
if not os.path.isdir(sourcePath):
	pathError = 1
	print "   [ERROR] soruce path doesn't exist!"
else:
	print "   Source path exists!"

if pathError == 1:
	print ""
	print "Path error, can't continue"
	exit()

directoryList = []
fileList = []

#save contents of source into fileList, excluding those without .kicad_mod
for filename in os.listdir(sourcePath):
	if filename[len(filename) - 10:] == ".kicad_mod":
		fullFilePath = filename
		print "file:",
		print fullFilePath,
		if searchTermString != "undef":
			if filename.find(searchTermString, 0, len(filename)) != -1:
				#found match
				fileList.append(fullFilePath)
				print ""
			else:
				print "[IGNORED]"
		else:
			fileList.append(fullFilePath)
			print ""

if subArgString == "1":
	#Save contents of source into directoryList, only choosing files with .pretty
	for filename in os.listdir(sourcePath):
		if filename[len(filename) - 7:] == ".pretty":
			fullFilePath = filename
			directoryList.append(fullFilePath)
	#extend fileList with subdirs
	for directoryname in directoryList:
		print "directory:",
		print directoryname
		for filename in os.listdir(sourcePath + "\\" + directoryname):
			if filename[len(filename) - 10:] == ".kicad_mod":
				fullFilePath = directoryname + "\\" + filename
				print "   file:",
				print fullFilePath,
				if searchTermString != "undef":
					if filename.find(searchTermString, 0, len(filename)) != -1:
						#found match
						fileList.append(fullFilePath)
						print ""
					else:
						print "[IGNORED]"
				else:
					fileList.append(fullFilePath)
					print ""
	

#print fileList
#print directoryList

if justListArgs == 1:
	print ""
	print "Exiting (-l option used)"
	exit()
else:
	print "Running script..."

ensure_dir(destPath)
for dirname in directoryList:
	ensure_dir(destPath + dirname)
	
for filename in fileList:
	print ""
	print "Opening",
	fullFilePath = sourcePath + filename
	print fullFilePath
	# Open the export mod style file
	if os.path.isfile(fullFilePath) == True:
		statinfo = os.stat(fullFilePath)
		workingFileHandle = open(fullFilePath, "r")
		# Read the footprint to memeory
		workingFileMemory = workingFileHandle.read()
		#  ..Now workingFileMemory is a string that is the input file
		
		
		#First, seek out initial "pad" text
		locVar = workingFileMemory.find("(pad ", 0, len(workingFileMemory))
		if locVar > 0:
			#This file has one or more
			fileVar = 0
			parsingFile = 1
			while parsingFile == 1 and fileVar < len(workingFileMemory):
				locVar = workingFileMemory.find("(pad ", fileVar, len(workingFileMemory))
				if locVar > 0:
					#print "Found pad!"
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
						workOnPad = 0
						if leftParenCount == rightParenCount:
							print "Found: ",
							if workingFileMemory.find("(at 0 0)", leftParen, nextParen) > 0:
								#This is a center pad
								print "Center,",
								if nopadArgString != "CENTER":
									print "(will modify)",
									#work on this pad
									workOnPad = 1
								else:
									countIsNonZero = 0 #break
									print "(ignored)"
							if workingFileMemory.find("(at 0 0)", leftParen, nextParen) == -1:
								print "Normal,",
								#This is not a center pad
								if onlypadArgString != "CENTER":
									print "(will modify)",
									#work on this pad
									workOnPad = 1
								else:
									countIsNonZero = 0 #break
									print "(ignored)"
						# Now test for the type of pad, but only after center rules adhered to
						if workOnPad == 1:
							workOnPad = 0
							if workingFileMemory.find(" smd ", leftParen + 4, nextParen) > 0: #adding 4 insures pad named 'smd' doesn't trigger
								#This is a smd pad
								print "Type: SMD",
								if padArgString == "SMD":
									print "(will modify)"
									#work on this pad
									workOnPad = 1
								else:
									countIsNonZero = 0 #break
									print "(ignored)"
							if workingFileMemory.find(" thru_hole ", leftParen + 4, nextParen) > 0: #adding 4 insures pad named 'thru_hole' doesn't trigger
								#This is a thru_hole pad
								print "Type: PTH",
								if padArgString == "PTH":
									print "(will modify)"
									#work on this pad
									workOnPad = 1
								else:
									countIsNonZero = 0 #break
									print "(ignored)"
							if workingFileMemory.find(" np_thru_hole ", leftParen + 4, nextParen) > 0: #adding 4 insures pad named 'np_thru_hole' doesn't trigger
								#This is a np_thru_hole pad
								print "Type: NPTH",
								if padArgString == "NPTH":
									print "(will modify)"
									#work on this pad
									workOnPad = 1
								else:
									countIsNonZero = 0 #break
									print "(ignored)"
							
						if workOnPad == 1:
							countIsNonZero = 0
							rightParen = nextParen + 1
	#						print "Syntax Correct!"
	#						print workingFileMemory[leftParen:rightParen]
	
#This is where the options on what to do take place.
#If rem is used, remove the pad layer
							if remArgString != "undef":
								#We will be removing a layer
								#Generate string data
								# find .
								var3 = remArgString.find(".", 0, len(remArgString))
								if var3 != -1:
									searchString = " *." + remArgString[var3+1:]
									replaceString = " F." + remArgString[var3+1:] + " B." + remArgString[var3+1:]
									removeString = " " + remArgString
									#Look for the (layers .....) param
									var1 = workingFileMemory.find("(layers ", leftParen, rightParen)
									var2 = workingFileMemory.find(")", var1, rightParen)
									#convert *.thing to F.thing and B.thing
									var3 = workingFileMemory.find(searchString, var1, var2)
									if var3 != -1:
										tempFileMemory = workingFileMemory[:var3] + workingFileMemory[var3 + len(searchString):]
										#Move pointers
										rightParen -= len(searchString)
										var2 -= len(searchString)
										#Now insert new text
										#print tempFileMemory[leftParen:rightParen]
										workingFileMemory = tempFileMemory[:var3] + replaceString + tempFileMemory[var3:]
										rightParen += len(replaceString)
										var2 += len(replaceString)
										#print workingFileMemory[leftParen:rightParen]
									#Search for string to remove
									var4 = workingFileMemory.find(removeString, var1, var2)
									if var4 != -1:
										tempFileMemory = workingFileMemory[:var4] + workingFileMemory[var4 + len(removeString):]
										workingFileMemory = tempFileMemory
										rightParen -= len(removeString)
										var2 -= len(removeString)
										#print workingFileMemory[leftParen:rightParen]
#If add was used, add the layer if it doesn't already exist
							if addArgString != "undef":
								#We will be adding a layer
								# find .
								var3 = addArgString.find(".", 0, len(addArgString))
								if var3 != -1:
									#Generate string data
									searchString = " *." + addArgString[var3+1:]
									addString = " " + addArgString
									#Look for the (layers .....) param
									var1 = workingFileMemory.find("(layers ", leftParen, rightParen)
									var2 = workingFileMemory.find(")", var1, rightParen)
									#if *.thing is found, we are done!
									var3 = workingFileMemory.find(searchString, var1, var2)
									if var3 != -1:
										# *. was found!  the arg is covered.
										var3 = var3
									else:
										# *. not found, but perhaps the single one is there
										var3 = workingFileMemory.find(addString[1:], leftParen, rightParen)
										if var3 != -1:
											#found it, we are done
											var3 = var3
										else:
											#we need to add it.
											tempFileMemory = workingFileMemory[:var2] + addString + workingFileMemory[var2:] 
											rightParen += len(addString)
											var2 += len(addString)										
											workingFileMemory = tempFileMemory
											#print workingFileMemory[leftParen:rightParen]
#If mod was used, remove the attrib and reapply it.
							if modArgString != "undef" and modArgValueMMString != "undef":
								#We will be modifying a parameter
								#Generate string data
								searchString = "undef"
								if modArgString == "PadClearance":
									searchString = "(clearance"
								if modArgString == "MaskClearance":
									searchString = "(solder_mask_margin"
								if modArgString == "PasteClearance":
									searchString = "(solder_paste_margin"
								
								if searchString != "undef":
									#good to go!
									addString = searchString + " " + modArgValueMMString + ")"
									
									#Look for instance of search term
									var3 = workingFileMemory.find(searchString, leftParen, rightParen)
									if var3 != -1:
										#found it -- index it
										var1 = workingFileMemory.find(searchString, leftParen, rightParen)
										var2 = workingFileMemory.find(")", var1, rightParen)
										#Calculate length of this string
										stringLen = var2 - var1 + 1
										#remove it
										tempFileMemory = workingFileMemory[:var1] + workingFileMemory[var1 + stringLen:]
										workingFileMemory = tempFileMemory
										rightParen -= stringLen
										var2 -= stringLen
										#var1 should now equal var2
										
									#Now add the new tag
									if workingFileMemory[rightParen - 2] != " ":
										tempString = " " + addString
										addString = tempString
									tempFileMemory = workingFileMemory[:rightParen - 1] + addString + workingFileMemory[rightParen - 1:] 
									rightParen += len(addString)
									var2 += len(addString)										
									workingFileMemory = tempFileMemory
									#print workingFileMemory[leftParen:rightParen]
								else:
									print "Invalid modArgString"
				else:
					parsingFile = 0
	#		print workingFileMemory[locVar-3:locVar+3]
		else:
			#This file has none!
			print "File has no pads!"
    
		#print tempFileMemory
		#programPause = raw_input("Press the <ENTER> key to continue...")
    
		#Write the output file
		outputFilePath = destPath + filename
		# Write out the workingFileMemory
		if os.path.isfile(outputFilePath) == True:
			statinfo = os.stat(outputFilePath)
			outputFileHandle = open(outputFilePath, "w+")
			# Read the KiCad Library to memeory
		else:
			print "creating",
			print outputFilePath
			outputFileHandle = open(outputFilePath, "w+")
		outputFileHandle.write(workingFileMemory) # Enable this line to write memory to OUTPUT
		outputFileHandle.close()
		
		workingFileHandle.close()
	else:
		print "File not opened!"
    
	print ""

print "Script finished!"