SparkFun Electronics KiCad Libraries
====================================

This repository is to contain a KiCad conversion of the "post-DFM" cleanup of the SparkFun-Eagle-Libraries.

Current status and tasks
----------------

* **[DONE]** Create this repo
* Research import scripts
* Perform Bulk import of SparkFun-Eagle-Libraries
* Create set of accepted footprints
* Create equivilent libraries in this repo
* Link libraries to footprints
* Check documentation is OK
* Consider 3D models.

Contents
-------------------

* /Conversion -- Information and scripts having to do with converting eagle components to KiCad (See contained README.md)
* README.md -- This file

Resource
----------------

* [The KiCad site](http://kicad-pcb.org/)

**KiCad installation**

* Uninstall previous versions of KiCad
* Download KiCad stable version 4.0.5 from [http://kicad-pcb.org/download/](http://kicad-pcb.org/download/windows/) and install
* After install, you'll be prompted to install "Wings 3D", check this box to be redirected to [http://www.wings3d.com/](http://www.wings3d.com/)
* Download and install the stable release 2.1.5

**Using the libraries**

* Create a local project (this is necessary because projects hold library path information)
* Open the "Schematic Library Editor"
* Prefrences -> Component Libraries
  * Remove all libraries from list
  * Add -> navigate to SparkFun-KiCad-Libraries -> select all .lib files -> open, then hit OK
  * Test by selecting an active library.  All sparkfun libraries should be displayed.  Close the library editor
* Open the "PCB Footprint Editor"
* Prefrences -> Footprint Library Manager
  * Remove all (if any) libraries, hit OK
* Prefrences -> Footprint Libraries Wizard
  * Next (files on my computer)
  * Navigate to SparkFun-KiCad-Libraries -> select all .mod files and hit ok
  * Next
  * Select for this project only
  * Next
  * Close the editor
* Save the project (Green arrow into extern HDD icon, no menu exists)

Now, This project is linked to the libraries.  Open a schematic and place components.  See kicad enginursday post for converting from schematic into board (Note: You need to have nets for this to work... not just unconnected components)
License Information
-------------------

This library is released under the [Creative Commons ShareAlike 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/) license. 
**You are welcome to use this library for commercial purposes.**
For attribution, we ask that when you begin to sell your device using our footprint, you email us with a link to the product being sold. 
We want bragging rights that we helped (in a very small part) to create your 8th world wonder. 
We would like the opportunity to feature your device on our homepage.

Please consider contributing back to this library or others to help the open-source hardware community continue to thrive and grow! 
