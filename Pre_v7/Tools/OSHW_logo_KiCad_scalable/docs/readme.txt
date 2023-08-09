
The 'OSHW_logo_orig.emp' file results in a silkscreen logo with
about 1.18in height, which may be too large for your project.

Use the scale.pl script to resize it:

scale.pl OSHW_logo_orig.emp new_logo.emp <layer> 5.0mm

or 

scale.pl OSHW_logo_orig.emp new_logo.emp <layer> 0.5in


Replace <layer> with the KiCad layer you need.

Top copper:     15
Top silkscreen: 21

To move the object to bottom copper/silkscreen, just place
the curser over the logo and press 'F' for flip in pcbnew.


Now start kicad/pcbnew, go into the library/footprint editor
("open module editor", it's the icon left to the scissors looking
like a DIP chip) and click on the "import module" icon, select
the .emp file of your choice and click OK.

If you want to finish quickly, just click on the "insert module
into current board icon" (it's the one with the yellow star).

Place the logo where you need it. If the size is still not correct,
repeat at the beginning.

If the logo doesn't show up on your gerber files, your version
of kicad still suffers from bug #792399.

