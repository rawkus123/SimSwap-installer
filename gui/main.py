from pathlib import Path  # core python module
import PySimpleGUI as sg  # pip install pysimplegui
import os
import shutil
import subprocess
#import platform

#ostype = platform.system()

user_profile = os.environ['USERPROFILE']
SimSwap = user_profile + "/miniconda3/envs/SimSwap/"

pathsingle = './script.txt'

if os.path.isfile(pathsingle) == True:
    os.remove('script.txt')

def is_valid_path(filepath):
    if filepath and Path(filepath).exists():
        return True
    sg.popup_error("Filepath not correct")
    return False

def main_window():

    column_to_be_centered = [[sg.Text('Please chose a script from "Scripts Menu"')],
                [sg.Button('Exit')]]

    menu_def = [["Scripts", ["Single Swap", "MultiSwap", "Specific Swap"]],
                ["Help", ["Help","Exit"]]]

    layout = [[sg.MenubarCustom(menu_def, tearoff=False)],
              [[sg.VPush()],
              [sg.Push(), sg.Column(column_to_be_centered,element_justification='c'), sg.Push()],
              [sg.VPush()]]
            ]

    window = sg.Window("SimSwap", layout, use_custom_titlebar=True)

    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, "Exit"):
            break

        if event in ("Single Swap"):
           
            scripttype = "./core/single.txt"
            shutil.copy(scripttype, "./script.txt")
            
            layout = [[sg.MenubarCustom(menu_def, tearoff=False)],
              [sg.T("Input Picture A:", s=15, justification="r"), sg.I(key='-IN1-',enable_events=True), sg.FileBrowse(file_types=(("Pictures", "*.png;*.jpg"),))],
              [sg.T("Input Video:", s=15, justification="r"), sg.I(key='-IN2-'), sg.FileBrowse(file_types=(("Mp4 Videos", "*.mp4"),))],
              [sg.T("Output Folder:", s=15, justification="r"), sg.I(key='-OUT-'), sg.FileSaveAs()],
              [sg.Exit(s=16, button_color="tomato"),sg.B("Start", s=16)],
            ]
            noIN3 = True
            window.close()
            window = sg.Window("SimSwap - Single Swap", layout, use_custom_titlebar=True)
            event, values = window.read()

        if event in ("MultiSwap"):
            scripttype = "./core/multi.txt"
            shutil.copy(scripttype, "./script.txt")
            layout = [[sg.MenubarCustom(menu_def, tearoff=False)],
              [sg.T("Input Picture A:", s=15, justification="r"), sg.I(key='-IN1-',enable_events=True), sg.FileBrowse(file_types=(("Pictures", "*.png;*.jpg"),))],
              [sg.T("Input Video:", s=15, justification="r"), sg.I(key='-IN2-'), sg.FileBrowse(file_types=(("Mp4 Videos", "*.mp4"),))],
              [sg.T("Output Folder:", s=15, justification="r"), sg.I(key='-OUT-'), sg.FileSaveAs()],
              [sg.Exit(s=16, button_color="tomato"),sg.B("Start", s=16)],
            ]
            window.close()
            window = sg.Window("SimSwap - Multi Swap", layout, use_custom_titlebar=True)
            noIN3 = True
            event, values = window.read()

        if event in ("Specific Swap"):
            scripttype = "./core/specific.txt"
            shutil.copy(scripttype, "./script.txt")
            layout = [[sg.MenubarCustom(menu_def, tearoff=False)],
              [sg.T("Input Picture A:", s=15, justification="r"), sg.I(key='-IN1-',enable_events=True), sg.FileBrowse(file_types=(("Pictures", "*.png;*.jpg"),))],
              [sg.T("Specific Face to Swap:", s=15, justification="r"), sg.I(key='-IN3-',enable_events=True), sg.FileBrowse(file_types=(("Pictures", "*.png;*.jpg"),))],
              [sg.T("Input Video:", s=15, justification="r"), sg.I(key='-IN2-'), sg.FileBrowse(file_types=(("Mp4 Videos", "*.mp4"),))],
              [sg.T("Output Folder:", s=15, justification="r"), sg.I(key='-OUT-'), sg.FileSaveAs()],
              [sg.Exit(s=16, button_color="tomato"),sg.B("Start", s=16)],
            ]
            window.close()
            window = sg.Window("SimSwap - Specific Swap", layout, use_custom_titlebar=True)
            noIN3 = False
            event, values = window.read()

        if event in ("Start"):
            event, values = window.read()
            if noIN3 == False:
                picA, vidA, outA, picB = values['-IN1-'], values['-IN2-'], values['-OUT-'], values['-IN3-']
            else:
                picA, vidA, outA= values['-IN1-'], values['-IN2-'], values['-OUT-']
                contpicb = False

            f1 = open('script.txt','r')
            f2 = f1.read()
            f1.close()
            f3 = f2.replace("picA",picA)
            f1 = open('script.txt','w')
            f1.write(f3)
            f1.close()
            v1 = open('script.txt','r')
            f2 = v1.read()
            v1.close()
            f3 = f2.replace("vidA",vidA)
            f1 = open('script.txt','w')
            f1.write(f3)
            f1.close()
            o1 = open('script.txt','r')
            f2 = o1.read()
            o1.close()
            f3 = f2.replace("outA",outA)
            f1 = open('script.txt','w')
            f1.write(f3)
            f1.close()
            p1 = open('script.txt','r')
            f2 = p1.read()
            p1.close()
            
            if contpicb != False:
                f3 = f2.replace("picB",picB)
                f1 = open('script.txt','w')
                f1.write(f3)
                f1.close()
            
            os.remove('./script.bat')
            os.rename('script.txt','script.bat')
            subprocess.call([r'script.bat'])
            
        #window.close()


if __name__ == "__main__":
    SETTINGS_PATH = Path.cwd()
    # create the settings object and use ini format
settings = sg.UserSettings(
        path=SETTINGS_PATH, filename="config.ini", use_config_file=True, convert_bools_and_none=True
    )
theme = settings["GUI"]["theme"]
font_family = settings["GUI"]["font_family"]
font_size = int(settings["GUI"]["font_size"])
sg.theme(theme)
sg.set_options(font=(font_family, font_size))
main_window()


