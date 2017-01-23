Conversion tools and information
====================================

This directory contains information regarding getting the libraries transfered from eagle to kicad.

Tasks:

* Convert bulk of libraries to Kicad
* Combine footprints and have single source for common footprints
* Convert .mod to new format: .pretty (.kicad_mod)
* Determine where the descriptions and prod IDs should live

**Convert bulk of libraries/boards to Kicad**

Use this script for libraries

https://github.com/lachlanA/eagle-to-kicad-libs

Use this script for boards

https://github.com/lachlanA/eagle-to-kicad

**Note:** This is very hacky.  It would be best to establish the proper libraries first, then link to those rather than have the script spit out specific libs for each board.  This insures the resultant file is consistent with the KiCad libraries.

**Combine footprints and have single source for common footprints**

A tool for moving symbols and footprints between .mod and .lib files:

http://www.compuphase.com/electronics/kicadlibrarian_en.htm

**Convert .mod to new format: .pretty (.kicad_mod)**

Do this by "saving as" within kicad

**Determine where the descriptions and prod IDs should live**

The descriptions are not formatted as well but do show up on the part browser.  The product IDs could be added as keywords (and would be indexed for searching).

![alt text](https://github.com/sparkfun/SparkFun-KiCad-Libraries/blob/master/Conversion/description_tag_example.jpg?raw=true "Example description")

A better location for the PROD_IDs would be as a field of the components (probably the symbol).  This can also be edited in the schematic as shown:

![alt text](https://github.com/sparkfun/SparkFun-KiCad-Libraries/blob/master/Conversion/fieldsView.jpg?raw=true "Example description")

The BOM generation script will need to be adjusted to output the extra fields in a useful way.

File format:

https://en.wikibooks.org/wiki/Kicad/file_formats#Schematic_Libraries_Files_Format

*the hardest part of any task is starting* 
