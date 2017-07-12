## Pad Modification Script

The script KiCadPadMod.py modifies KiCad model files.  It operates on pads and can change parameters as configured with options.

Features:

* Operate on SMD, PTH, or NPTH per each pass
* Exclude, or only operate on, pads at origin
* Add or remove paste or mask layers
* modify pad clearance, mask margin, or paste margin

### Syntax

Running the script by itself is not useful.  Instead, kludge together option lists in a batch file and run it that way for the options you want.

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

These allow you to add or subtract pad parameters.

**-mod [PadClearance|MaskClearance|PasteClearance] [*value*]**

This allows you to modify clearances.  Using -mod will change any existing values, or add a new value if none exists.

**[input directory]**

Full path to the directory that the .kicad_mod and .pretty files are, requires trailing slash

**[output directory]**

Full path to the directory where the modified files will be saved.  Directory structure will match [input path]

**[(optional search term)]**

Add a partial file name here.  The script will only apply to filenames that contain the search term.  This can be a whole file name, or part (like 0603).  All directories will be searched if -sub 1

### Usage

All arguments are shown here, though the command is invalid and will fail the checks:

* `python KiCadPadMod.py -l -sub 0 -pad SMD -nopad CENTER -onlypad CENTER -add F.Mask -rem F.Paste -mod PadClearance 0.004 C:\temp\input\ C:\temp\output\ 0603`

This example says, root folder only, operate on all PTH pads and add a F.Mask layer:

* `python KiCadPadMod.py  -sub 0 -pad PTH -add F.Mask C:\temp\input\ C:\temp\output\`

This says, dry run remove all F.Paste from only the center pad of root and subdirectories:

* `python KiCadPadMod.py -l -sub 1 -pad NPTH -onlypad CENTER -rem F.Paste C:\temp\input\ C:\temp\output\`

**Batch usage**

This batch file is used to remove all paste from all PTH and NPTH holes:

```dos
REM This is used to remove all paste from all sparkfun libs (Note: Took 1min 27s)
REM Manualy put the output into the input after checking results.

python KiCadPadMod.py -sub 1 -pad PTH -rem F.Paste C:\github\SparkFun-KiCad-Libraries\Footprints\ C:\temp\output\
python KiCadPadMod.py -sub 1 -pad PTH -rem B.Paste C:\temp\output\ C:\temp\output2\
python KiCadPadMod.py -sub 1 -pad NPTH -rem F.Paste C:\temp\output2\ C:\temp\output3\
python KiCadPadMod.py -sub 1 -pad NPTH -rem B.Paste C:\temp\output3\ C:\temp\output4\
```