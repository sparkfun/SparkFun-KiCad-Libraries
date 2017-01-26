Conversion tools and information
====================================

This directory contains information regarding getting the libraries transfered from eagle to kicad.

Tasks:

* Convert bulk of libraries to Kicad
* Combine footprints and have single source for common footprints
* Convert .mod to new format: .pretty (.kicad_mod)
* Determine where the descriptions and prod IDs should live

### Convert bulk of libraries/boards to Kicad

Use this script for libraries

https://github.com/lachlanA/eagle-to-kicad-libs

Use this script for boards

https://github.com/lachlanA/eagle-to-kicad

**Note:** This is very hacky.  It would be best to establish the proper libraries first, then link to those rather than have the script spit out specific libs for each board.  This insures the resultant file is consistent with the KiCad libraries.

#### Analysis of naming

In order to write a script, it must link parts from two files.  It seems the only way to do that is by using the name of the component/footprint/etc, so let's explore that.  Using these eagle export scripts, there are a few options for naming convention.

.. But first let's see what happened to a highly nested component in eagle... the 10uF cap.  In eagle, the part is called "10UF" and has sub-parts -0603-... etc for all packages.  In KiCad the symbol is called "10UF" and there are 4 suggested footprints within the footprint filter that are generated, 0603, 0805, 1206, 1210.  This is kind of a problem because I really want to retain a prod_id for each package, so these will need to be un-nested.

To solve this, during library export select the drop down "Combine Parts/package variants where possible" and choos "Out put new part for every foot print type" instead.  The result is that each variant now has it's own (duplicate) symbol.  (note: the filter is still filled with all possible footprints.  **This will need to manualy be fixed**)

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
