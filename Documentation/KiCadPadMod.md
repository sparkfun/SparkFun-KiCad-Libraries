## Pad Modification Script

The script KiCadPadMod.py modifies KiCad model files

### Syntax

Running the script by itself is not useful.  Instead, kludge together massive option lists in a batch file and run it that way for the options you want.

`KiCadPadMod [options list] [input directory] [output directory] [(optional search term)]`

### Options

Each option may or may not be followed by data.

Options must occur in the order listed

**-l**

List.  This option prevents the script from actually running anything and instead returns the passed options as decoded, as well as detected files if specified.

**-sub [0|1]**

Sublevel to search for .kicad_mod files.  Using 0 searches only the passed directory.  Using 1 searches all folders within the passed directory.  This is usefull to batch edit an entire collection of .pretty folders.

**-pad [SMD|PTH|NPTH]**

Choose the type of pad to operate on.

**-nopad [CENTER]**

Exclude pads at 0,0 from the search.

**-onlypad [CENTER]**

Only operate on pads at 0,0.

**-add [F.Paste|B.Paste|F.Mask|B.Mask]**

**-rem [F.Paste|B.Paste|F.Mask|B.Mask]**

**-mod [PadClearance|MaskClearance|PasteClearance] [*value*]**

These allow you to add or subtract pad parameters, as well as modify clearances.

TODO: Implement mod operation

**[input directory]**

Full path to the directory that the .kicad_mod and .pretty files are, requires trailing slash

**[output directory]**

Full path to the directory where the modified files will be saved.  Directory structure will match [input path]

**[(optional search term)]**

Add a partial file name here.  The script will only apply to filenames that contain the search term.  This can be a whole file name, or part (like 0603)

TODO: Complete this function

### Usage

All arguments are shown here, though the command is invalid and will fail the checks:

* `python KiCadPadMod.py -l -sub 0 -pad SMD -nopad CENTER -onlypad CENTER -add F.Mask -rem F.Paste -mod PadClearance 0.004 C:\temp\input C:\temp\output 0603`

This example says, root folder only, operate on all PTH pads and add a F.Mask layer:

* `python KiCadPadMod.py  -sub 0 -pad PTH -add F.Mask C:\temp\input\ C:\temp\output\`

This says, dry run remove all F.Paste from only the center pad of root and subdirectories:

* `python KiCadPadMod.py -l -sub 1 -pad NPTH -onlypad CENTER -rem F.Paste C:\temp\input\ C:\temp\output\`