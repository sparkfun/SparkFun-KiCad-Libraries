Conversion tools and information
====================================

**This is an outdated readme**

## Process

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

## Notes that led to the above process

### Convert bulk of libraries/boards to Kicad

Use this script for libraries

https://github.com/lachlanA/eagle-to-kicad-libs

Use this script for boards

https://github.com/lachlanA/eagle-to-kicad

**Note:** This is very hacky.  It would be best to establish the proper libraries first, then link to those rather than have the script spit out specific libs for each board.  This insures the resultant file is consistent with the KiCad libraries.

#### Analysis of part naming

In order to write a script, it must link parts from two files.  It seems the only way to do that is by using the name of the component/footprint/etc, so let's explore that.  Using these eagle export scripts, there are a few options for naming convention.

.. But first let's see what happened to a highly nested component in eagle... the 10uF cap.  In eagle, the part is called "10UF" and has sub-parts -0603-... etc for all packages.  In KiCad the symbol is called "10UF" and there are 4 suggested footprints within the footprint filter that are generated, 0603, 0805, 1206, 1210.  This is kind of a problem because I really want to retain a prod_id for each package, so these will need to be un-nested.

To solve this, during library export select the drop down "Combine Parts/package variants where possible" and choose "Out put new part for every foot print type" instead.  The result is that each variant now has it's own (duplicate) symbol.  (note: the filter is still filled with all possible footprints.  **This will need to manualy be fixed**)

For instance, eagle part in file "SparkFun-Capacitors.lbr", the 10UF is:

* "deviceset name="10UF" prefix="C""
  * "device name="-0603-6.3V-20%" package="0603""
  * "device name="-1206-6.3V-20%" package="1206""
  * "device name="-0805-10V-10%" package="0805""
  * "device name="-1210-50V-20%" package="1210""

The resultant parts in KiCad are named:

* 10UF-0603-6.3V-20%
* 10UF-1206-6.3V-20%
* 10UF-0805-10V-10%
* 10UF-1210-50V-20%

.. The superfluous filters are mitigated by a new field "Footprint" which contains "0805", etc.

The conclusion is that the script must identify parts by the part-per-footprint names within the exported libraries for application of prod_id fields.

#### Analysis of library naming

Let's again look at "SparkFun-Capacitors.lbr".  After export, two files are created:

* SparkFun-Capacitors.lib
* SparkFun-Capacitors.mod

When the .lib is re-saved, two files are produced (could be renamed here):

* SparkFun-Capacitors.lib -- library of symbols and fields and stuff
* SparkFun-Capacitors.dcm -- Description and some other stuff

When the .mod is re-saved, a directory is created as such:

* somename.pretty
  * 0402.kicad_mod
  * 0603.kicad_mod
  * 0603-POLAR.kicad_mod
  * ... etc.
  
### Combine footprints and have single source for common footprints

A tool for moving symbols and footprints between .mod and .lib files:

http://www.compuphase.com/electronics/kicadlibrarian_en.htm

### Convert .mod to new format: .pretty (.kicad_mod)

Do this by "saving as" within kicad

### Determine where the descriptions and prod IDs should live

The descriptions are not formatted as well but do show up on the part browser.  The product IDs could be added as keywords (and would be indexed for searching).

![alt text](https://github.com/sparkfun/SparkFun-KiCad-Libraries/blob/master/Conversion/description_tag_example.jpg?raw=true "Example description")

A better location for the PROD_IDs would be as a field of the components (probably the symbol).  This can also be edited in the schematic as shown:

![alt text](https://github.com/sparkfun/SparkFun-KiCad-Libraries/blob/master/Conversion/fieldsView.jpg?raw=true "Example description")

With a special BOM plugin, the output CSV contains the extra fields:

![alt text](https://github.com/sparkfun/SparkFun-KiCad-Libraries/blob/master/Conversion/generatedBOM.jpg?raw=true "Example description")

File format:

https://en.wikibooks.org/wiki/Kicad/file_formats#Schematic_Libraries_Files_Format

------

*the hardest part of any task is starting* 
