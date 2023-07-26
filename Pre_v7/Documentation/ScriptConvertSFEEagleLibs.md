Conversion tools and information
====================================

This file describes the process of converting the DFM guided SparkFun-Eagle-Libraries repo to kicad format, while maintaining DFM guidelines.

## Process

**Make sure repo is in "C:\github\SparkFun-KiCad-Libraries"**

This is the evolving breakdown of tasks required to transfer the full set of sparkfun libraries.

* Convert bulk of libraries to Kicad *Manual operation*
  * Use "Out put new part for every foot print type" in lachlanA's ULP
* Use .bat file to run script for all libraries (check paths within)
  * Use custom script to (for each Eagle .lbr):
    * Detag and copy descriptions to .dcm files
    * Add fields for PROD_ID for each KiCad part
    * Add PROD_ID keyword for each part
	  * If not found, apply XXX-00000 for prod id
    * Scrub errant footprint filters by reference Footprint field
    * Report statistics to validate script operation
* Load and save-as for all .mod files to convert to .pretty format. *Manual operation*
* Combine all .mod files to a single .pretty folder. *Manual operation*
  * There will be duplicate file names (should be identical)
  * There will be similar footprint .mod files (should be identical)
* Weed out (about 3) spare F8 commands that were not saved correctly in the lib files (KiCad will tell you they are broken)
* Convert line graphics of .kicad_mod files to poly graphics using other bat
  * Output ends up in Export.pretty
  * When satisfied, overwrite Sparkfun.pretty with contents of Export.pretty

### Convert bulk of libraries/boards to Kicad

This task is done from within eagle.  Open each library and run the conversion .ulp file ../Tools/eagle-to-kicad_ulp/eagle-lbr2kicad-1.0.ulp.  This is a modified version of lachlanA's script, from https://github.com/lachlanA/eagle-to-kicad-libs.

During this stage, select

* "Output a new part for every footprint type"
* "Don't prefix the library name to the footprint name in module"

for each library.

When complete

* move the log files to ../Tools/SparkFun-Eagle-Libraries_Conversion/EagleExportLogs
* Copy .lib and .mod files to ../Libraries
* Delete originals when you are happy

### Use batch files to convert internal part names and DFM stuff

Run ../Tools/SparkFun-Eagle-Libraries_Conversion/Python/RunOnExportedLibs.bat.

The following files will be made and placed within ../Libraries

* name.lib files
* name.dcm files
* ConvertSFELibsLog.txt

Move the log file to ../Tools/SparkFun-Eagle-Libraries_Conversion/PythonScriptLogs

### Load and save-as for all .mod files to convert to .pretty format.

* Create a new project in KiCad named something like "import_n*.
* Go into the footprint editor, manage libraries, and remove all.
* With the library wizard, append exported .mod files to project (not global)
* For each library,
  * Set library active
  * Save-as to location ../Footprints
  * Append with name (such as SparkFun-Aesthetics.mod)
    * Ex: C:\github\SparkFun-KiCad-Libraries\Footprints\Aesthetics.pretty

Tip:  copy base path to text doc for easy copy-paste.  Also, browse .mod folder to copy paste names.  This is truely the most painful part.

### Combine all .mod files to a single .pretty folder.

Call this /Footprints/SparkFun.pretty

When deciding which duplicated part name to use, ditch the most specific and keep the most generalized

### Weed out script failures

Load libraries into test KiCad project (AKA import_n.pro)

* Open schematic lib editor
* Remove all libs from library manager
* Add all .lib files from ../Libraries
* Click brows components
  * Will report error in file and line number.  Look for misplaced "F" commands
  * Move errant lines up to last "F" position, usually after F3
  * Rename F8 to F4

Tip: Open all .libs in notepad++ and search "F8" in all open files.

### Convert polys

Run ../Tools/SparkFun-Eagle-Libraries_Conversion/Python/ConvertLinesPolys.bat.

Files will go to: C:\github\SparkFun-KiCad-Libraries\Tools\SparkFun-Eagle-Libraries_Conversion\Export.pretty

Copy kicad_mod files back into SparkFun.pretty

## You are done enough!

At this point, libs should be useable.  Keepout is now on user layers, should be on other layer (script?)
