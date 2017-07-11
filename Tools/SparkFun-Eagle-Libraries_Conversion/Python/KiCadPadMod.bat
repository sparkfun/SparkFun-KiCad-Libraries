@ECHO OFF

REM "A full command line:"
REM python KiCadPadMod.py -l -sub 0 -pad SMD -nopad CENTER -onlypad CENTER -add F.Mask -rem F.Paste -mod PadClearance 0.004 C:\temp\input C:\temp\output 0603

python KiCadPadMod.py  -sub 0 -pad PTH -add F.Mask C:\temp\input\ C:\temp\output\

REM python KiCadPadMod.py -sub 1 -pad NPTH -onlypad CENTER -rem F.Paste C:\temp\input\ C:\temp\output\