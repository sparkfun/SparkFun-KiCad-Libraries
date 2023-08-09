## SFE Process for Board Design

### Prepare

Prerequisites:

* This repo is up-to-date
* SFE default settings are applied

Make a new project and save it to working /hardware directory.

### Schematic

Open the eeschema

Setup the frame:
* File -> Page Settings
* Import date (click <<<)
* Enter version number "v01"
* Enter board name
* Enter company name "SparkFun Electronics"

Set up the libraries
* Preferences -> Component Libraries
* Remove all
* Add all .lib files from this repo

**Draw schematic** - for this make LM1117 LDO circuit with two pin input, two pin output, input cap, output cap

#### Place symbols

Hotkeys

* '?' show hotkeys
* 'a' to add component
* 'p' to add power symbol
* 'r' to rotate
* 'x' and 'y' to mirror
* 'm' to pick up
* 'g' to drag (keeping wires)

Components

* 10UF 16V on input
* 10UF 6.3V on output
* LM1117
* 240 ohm resistor on high side
* 105 ohm to ground
* 2 2-position 0.1 inch headers
* Gnd from power symbols

#### Draw Nets

**Consolidate parts**

* Use 'g' to drag, 'm' to move.

**Clean up labels**

* Use 'm' over text
* Use 'e' to shorten text
* Orient PROD-IDs similarly and move to readable location (In this example, vertical text placed above works well)

**Name nets**

* Use 'l' to add label, use 1mm size, make sure point is attached to net (no floating labels)

This design has 4 nets:
* PWR_IN
* PWR_OUT
* FB
* GND

#### Prep for Layout

**Annotate symbols** -- Use annotate symbol button

**Associate components**

The first time this is run, no footprints exist.  Click through the dialogs.  Then go Preferences -> Footprint Libraries, click "Append with Wizard", group select all .pretty folders from this repo, and add.

Close the associate dialog and re-do now for auto part search

Select a footprint in the right-hand pane for each part.

Save the association, then close the dialog

Click "NET" button to generate a netlist, and save.

Save and close the schematic.

#### Setup Pcbnew

**Configure frame** - Use File -> Page Settings as in eeschema

**Import netlist**

Open Pcbnew

Use "Read Netlist button"

Click "Read Current Netlist"

Now you have a pile of parts in your frame.

**Build net class matrix**

Select Inches in left toolbar.

Open Design Rules -> Design Rules

Add two new classes:

* Bulk - 10 mils clearance, 16 mils width, 15 mils vias drill, 24 mils via size
* Signal - 8 mils clearance, 8 mils width, 15 mils vias drill, 24 mils via size

Assign nets:

* Add PWR_IN, PWR_OUT, and GND to bulk membership
* Add FB to signal membership

#### Perform layout

View must be set to default to organize parts.  Use menu or press F9.

Click IC with arrows (Mode: footprint)

Right click on component pile -> global spread and place -> spread out all footprints

**Arrange components**

Switch to opengl view (F12)

**Route Tracks**

Click on "Add tracks and vias" (Right bar)

"d" becomes drag track/via

**Add board edges**

Set grid to 50 mils

Set layer to "Edge cuts"

Select graphic line tool (Right bar)

Draw edges

**Add ground pours**

Select F.Cu layer

Select "Add filled regions" (Right bar)

Start drawing, will generate edit dialog

Select GND

Set min width, clearance

Finish drawing

Repeat on B.Cu

Save design

**Clean up board**

Press alt-3 - There's a bunch of excess text.

Hide unwanted text with 'e'

Some designs want designatiors on the silk for reference, if so move them where you like.

View hidden text through render tab in right bar.

**Go back and add a SparkFun logo**

Save the design, close it, go back and open eeschema.  Add a SFE flame and OSH logo above the info box.  These are components so associate them, generate a netlist, and open that netlist back in pcbnew.  Then, arrange the silks.  Add some text too if you like, try 0.03x0.03 size.

**Add standoffs**

Just like the logos, standoffs have a symbol and footprint.

**Add stitching vias and fiducials**

From pcbnew, add a footprint directly ('o').

Vias are located in hardware.  Name it the correct net, hide the text, then copy.

Fiducials are located in aesthetics.

For both, select the zone frame and re-select fill to have it recalculate zone clearance.

