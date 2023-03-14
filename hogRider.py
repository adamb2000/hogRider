from winreg import *
import shutil
from os import getcwd

def findLocations():
    print("####################################################################################################################################################################")
    dir = getcwd() +"\hog_rider.wav"
    try:
        print(shutil.copy(dir, "C:\\Windows\\Media\\hog_rider.wav"))
        registry = ConnectRegistry(None, HKEY_CURRENT_USER)
        rawKey = OpenKey(registry, "AppEvents\Schemes\Apps\.Default")
        cont = True
        index = 0
        while(cont):
            try:
                addr = EnumKey(rawKey,index)
                rawKey2 = OpenKey(registry, "AppEvents\Schemes\Apps\.Default" + '\\' + addr)
                addr2 = EnumKey(rawKey2,0)
                rawKey3 = OpenKey(registry, "AppEvents\Schemes\Apps\.Default" + '\\' + addr + '\\' + addr2)
                try:
                    print("AppEvents\Schemes\Apps\.Default" + '\\' + addr + '\\' + addr2)
                    t = EnumValue(rawKey3,0)
                    SetValue(rawKey2,addr2, REG_SZ, "C:\\Windows\\media\\hog_rider.wav")
                except:
                    print("error")
                index += 1
            except:
                cont = False
    except:
        print("ERROR")



    

findLocations()

