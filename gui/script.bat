Set venv=SimSwap

call %USERPROFILE%\miniconda3\Scripts\Activate %USERPROFILE%\miniconda3 
call activate %venv%
cd %USERPROFILE%\miniconda3\envs\SimSwap
call %USERPROFILE%\miniconda3\envs\SimSwap\python.exe test_video_swapsingle.py --crop_size 512 --use_mask --name people --Arc_path ./arcface_model/arcface_checkpoint.tar --pic_a_path "E:/Anaconda_ENV/SimSwap installer/Stacey.png" --video_path "" --output_path "" --temp_path ".\output_temp\"