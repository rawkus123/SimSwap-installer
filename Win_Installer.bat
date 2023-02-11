@echo off
Call .\miniconda_installations\Miniconda3-latest-Windows-x86_64.exe /InstallationType=JustMe /AddToPath=0 /RegisterPython=0 /NoRegistry=1

echo Please Wait... Installing MiniConda3

:check
if exist %Userprofile%\miniconda3\Scripts\activate.bat (echo "Done") else goto:check	

	
Call Start .\Create_ENV.bat
exit

:check2
if exist %Userprofile%\miniconda3\env\SimSwap (echo "Done") else goto:check2

Call Start .\Run_SimSwap.bat

