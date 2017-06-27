Converting an entire design
====================================

How to convert eagle design to kicad
 
1. Download the SparkFun-KiCad-Libraries repo
2. Open design in eagle
3. From eagle schematic Run ‘Run-1st.ulp’ to start process
4. In first window (‘Add numbers to unnumbered part references’) verify that ULP file location text box points correctly to SparkFun-KiCad-Libraries\eagle-to-kicad repo
5. In 3rd window (‘Export Eagle Schematic’) verify that ULP file location text box points correctly to SparkFun-KiCad-Libraries\eagle-to-kicad repo
6. Click OK on all the various windows
7. Conversion should complete, usually with some warnings or errors but these can be ignored.

Open Kicad then open the .sch file of the project. Things to clean up in the schematic:
* Change page size to US letter (File->Page Setup)
* Remove the yellow frame
* Move contents of schematic into KiCad frame
* Add the device, logo, and power libraries to the project
* Remove and re-add correct OSHW logo from ‘Logo’ library
* Remove and re-add power/GND symbols from ‘Power’ library
* Remove and re-add any I2C connectors from ‘SparkX’ library (SparkFun-KiCad-Libraries repo \NewlyCreated’)

To Import the PCB Layout:
* Run PcbNew.exe directly from command prompt or navigate to it
* File-Open. Then select *.brd from the file type drop down (lower right corner)
* Open the original .brd file from the Eagle project
* 'File-Save As' into the KiCad project directory (wherever the *.pro file lives)

For more detailed instructions see https://github.com/lachlanA/eagle-to-kicad
