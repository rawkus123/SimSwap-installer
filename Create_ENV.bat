@echo off

Call %Userprofile%\miniconda3\Scripts\activate.bat %Userprofile%\miniconda3\

if exist SimSwap37.7z (
Call conda create -n SimSwap
Call conda deactivate
Start /wait .\App\7-Zip64\7z.exe x .\SimSwap37.7z -o%Userprofile%\miniconda3\envs\SimSwap\
) ELSE (
    echo(
    echo "CPU or GPU powered?"
    echo "1) GPU"
    echo "2) CPU"
    echo(
    
    If Errorlevel 2 Goto 2
    If Errorlevel 1 Goto 1

    CHOICE /M Select /C 12

    :2
    Goto GPU
    :1
    Goto CPU
)

:GPU
Call conda create --name SimSwap --file requirements-gpu.txt

:CPU
Call conda create --name SimSwap --file requirements-cpu.txt

exit