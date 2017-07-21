# Production Outputs

There isn't a file that can be loaded and used, or it hasn't been found yet.  Use these graphics to select settings.

## Generate Gerber Files

From PCBNEW, select File->Plot.  Make the following selections:

![plot settings](https://github.com/sparkfun/SparkFun-KiCad-Libraries/raw/master/Documentation/Pictures/PlotSettings.png)

*Settings for basic 2 layer board*

## Generate Drill Files

KiCad chooses a default, and we'll try it out.  Primarily, the format is a bit different and it generates a seperate file for PTH and NPTH holes, which is desireable.  If GP comes back with complaints about these formats, we should try new settings.

From PCBNEW, select File->Fabrication Outputs->.drl file

![Drill Settings](https://github.com/sparkfun/SparkFun-KiCad-Libraries/raw/master/Documentation/Pictures/DrillSettings.png)

*Settings to generate PTH and NPTH files*

## Check Files

Using gerbv, and OSH Park's import tool, the output files are rendered correctly.

See [/Example Project/outputs](https://github.com/sparkfun/SparkFun-KiCad-Libraries/tree/master/Documentation/Example%20Project/outputs) for the outputs from the example project.