@echo off
SET venv=SimSwap
SET "cdir=%cd%"
SET "picA=*.png"
SET "picB=*.jpg"


echo(
echo(
echo(
echo                                        Select Py Script
echo                            =======================================
echo(
echo 1) "Swap Single"
echo 2) "Swap Multi"
echo 3) "Swap Defined"
echo(

If Errorlevel 3 Goto 3
If Errorlevel 2 Goto 2
If Errorlevel 1 Goto 1

CHOICE /M Select /C 123

:3
Goto SWAPSINGLE
:2
Goto SWAPMULTI
:1
Goto SWAPDEFINED

:SWAPSINGLE

for %%a in (%picA%) do set FoundA=%%a
for %%b in (%picB%) do set FoundB=%%b

if [%FoundA%]==[] (
	if [%FoundB%]==[] (
		goto notfound
	)
)

if [%FoundA%]==[] GOTO SETB
if [%FoundB%]==[] GOTO SETA

:SETA
echo "Found %FoundA%"
SET thispic=%cdir%/%FoundA%
GOTO VIDEO
:SETB
echo "Found %FoundB%"
SET thispic=%cdir%/%FoundB%
GOTO VIDEO

:notfound
echo "Picture not found"
Set /P "PictureLocation=Specify Picture Location and Name:"
Set /P AREYOUSURE="Are you sure? %PictureLocation% (Y/[N])"
if /I "%AREYOUSURE%" NEQ "Y" GOTO SETPICLOCATION
:SETPICLOCATION
Set thispic=%PcitureLocation%


:VIDEO
SET "videoA=*.mp4"
for %%c in (%videoA%) do set FoundV=%%c
If [%videoA%]==[] (Echo "Found %FoundV%") else (GOTO VideoNotFound)
Set thisVideo=%cdir%/%videoA%
GOTO VideoOutputName

:VideoNotFound
Echo "Video Not Found"
Set /P "VideoLocation=Specify Video Location and Name:"
Set /P AREYOUSURE="Are you sure? %PictureLocation% (Y/[N])"
if /I "%AREYOUSURE%" NEQ "Y" GOTO SETVIDEOLOCATION

:SETVIDEOLOCATION
Set thisVideo=%VideoLocation%

:VideoOutputName
Set /P "VideoOutput=Video Output Name:"

call %USERPROFILE%\miniconda3\Scripts\activate %USERPROFILE%\miniconda3
call activate %venv%

cd %USERPROFILE%\miniconda3\envs\SimSwap

Call %USERPROFILE%\miniconda3\envs\SimSwap\python.exe test_video_swapsingle.py --crop_size 512 --use_mask --name people --Arc_path ./arcface_model/arcface_checkpoint.tar --pic_a_path "%thispic%" --video_path "%thisVideo%" --output_path "&cdir&\output\%Videooutput%" --temp_path "%cdir%\temp_results