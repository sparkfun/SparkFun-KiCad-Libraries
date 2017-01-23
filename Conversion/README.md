Conversion tools and information
====================================

This directory contains information regarding getting the libraries transfered from eagle to kicad.

Tasks:

* Convert bulk of libraries to Kicad
* Combine footprints and have single source for common footprints
* Convert .mod to new format: .pretty (.kicad_mod)
* Determine where the descriptions and prod IDs should live

**Convert bulk of libraries to Kicad**

Use this script for libraries

https://github.com/lachlanA/eagle-to-kicad-libs

Use this script for boards

https://github.com/lachlanA/eagle-to-kicad

**Combine footprints and have single source for common footprints**

A tool for moving symbols and footprints between .mod and .lib files:

http://www.compuphase.com/electronics/kicadlibrarian_en.htm

**Convert .mod to new format: .pretty (.kicad_mod)**

Do this by "saving as" within kicad

**Determine where the descriptions and prod IDs should live**

The descriptions are not formatted as well but do show up on the part browser.  The product IDs could be added as keywords (and would be indexed for searching).

![alt text](https://raw.githubusercontent.com/sparkfun/SparkFun-KiCad-libraries/master/Conversion/description_tag_example.jpg "Example description")

File format:

https://en.wikibooks.org/wiki/Kicad/file_formats#Schematic_Libraries_Files_Format

*the hardest part of any task is starting* 
