from winreg import *
import shutil
import pyuac
from os import getcwd
import pickle


def main():
    if not pyuac.isUserAdmin():
        print("Re-launching as admin!")
        pyuac.runAsAdmin()
        #createFile()
    else:
        createFile()        
    

def createFile():
    try:
        file = open('resetSounds.txt','x')
        file.close()
        findLocations()
    except:
        file = open('resetSounds.txt', 'rb')
        t = pickle.load(file)
        print(t)
        print("FILE ALREADY EXISTS")

    

def findLocations():
    dir = getcwd() +"\hog_rider.wav"
    reset = dict()
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
                addr3 = "AppEvents\Schemes\Apps\.Default" + '\\' + addr + '\\' + addr2
                try:
                    reset[addr3] = QueryValue(rawKey2,addr2)
                    SetValue(rawKey2,addr2, REG_SZ, "C:\\Windows\\media\\hog_rider.wav")
                except:
                    print("error")
                index += 1
            except:
                cont = False
                file = open('resetSounds.txt','wb')
                pickle.dump(reset,file)
                file.close()
    except:
        print("ERROR")

main()

