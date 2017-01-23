testLibrary.lib -- Symbol of an IC in a lib
testModels.mod -- Ouptut from eagle-kicad tool
testOutputPretty.pretty/SparkFun-IC-Memory-SO08.kicad_mod -- Result after opening and "saving-as".
testLibrary.dcm -- File generated after adding description and keywords in library editor, then saving.

This test shows:
* The old kicad format uses a SVG style syntax while the new ".pretty" is more human readable.
* Keywords can be added to link symbols to real sparkfun parts.  This can be done either in tool or with a script.