@ECHO OFF

REM "A full command line:"
REM python KiCadPadMod.py -l -sub 0 -pad SMD -nopad CENTER -onlypad CENTER -add F.Mask -rem F.Paste -mod PadClearance 0.004 C:\temp\input\ C:\temp\output\ 0603

REM python KiCadPadMod.py  -sub 0 -pad PTH -add F.Mask C:\temp\input\ C:\temp\output\

REM python KiCadPadMod.py -sub 1 -pad NPTH -onlypad CENTER -rem F.Paste C:\temp\input\ C:\temp\output\

REM python KiCadPadMod.py -l -sub 1 -pad SMD -nopad CENTER -mod MaskClearance 0.006 C:\temp\input\ C:\temp\output\ DFN-6

REM python KiCadPadMod.py -sub 1 -pad PTH -rem F.Paste C:\github\SparkFun-KiCad-Libraries\Footprints\ C:\temp\output\


REM This is used to remove all paste from all sparkfun libs (Note: Took 1min 27s)
REM Manualy put the output into the input after checking results.

REM python KiCadPadMod.py -sub 1 -pad PTH -rem F.Paste C:\github\SparkFun-KiCad-Libraries\Footprints\ C:\temp\output\
REM python KiCadPadMod.py -sub 1 -pad PTH -rem B.Paste C:\temp\output\ C:\temp\output2\
REM python KiCadPadMod.py -sub 1 -pad NPTH -rem F.Paste C:\temp\output2\ C:\temp\output3\
REM python KiCadPadMod.py -sub 1 -pad NPTH -rem B.Paste C:\temp\output3\ C:\temp\output4\


REM This removes the paste from SMD of jumpers only
python KiCadPadMod.py -sub 0 -pad SMD -rem F.Paste C:\github\SparkFun-KiCad-Libraries\Footprints\Jumpers.pretty\ C:\temp\Jumpers.pretty\