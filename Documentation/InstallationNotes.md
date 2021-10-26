Installation Notes
----------------

* [The KiCad site](http://kicad.org/)

**KiCad installation**

* Uninstall previous versions of KiCad
* Download KiCad stable version 4.0.5 from [http://kicad.org/download/](http://kicad.org/download/windows/) and install
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
* Preferences -> Footprint Library Manager
  * Remove all (if any) libraries, hit OK
* Preferences -> Footprint Libraries Wizard
  * Next (files on my computer)
  * Navigate to SparkFun-KiCad-Libraries -> select all .mod files and hit ok
  * Next
  * Select for this project only
  * Next
  * Close the editor
* Save the project (Green arrow into extern HDD icon, no menu exists)

Now, this project is linked to the libraries.  Open a schematic and place components.  See KiCad enginursday post for converting from schematic into board (Note: You need to have nets for this to work... not just unconnected components)

**License Information**
