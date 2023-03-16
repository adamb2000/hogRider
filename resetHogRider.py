from winreg import *
import pyuac
from os import remove
import pickle


def main():
    if not pyuac.isUserAdmin():
        print("Re-launching as admin!")
        pyuac.runAsAdmin()
        # file = open('./resetSounds.txt', 'rb')
        # resetSounds(pickle.load(file)) 
    else:
        file = open('./resetSounds.txt', 'rb')
        resetSounds(pickle.load(file))        
    
def resetSounds(reset):
    try:
        remove("C:\\Windows\\Media\\hog_rider.wav")
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
                    SetValue(rawKey2,addr2, REG_SZ, reset[addr3])
                    print("HWVBSDJ")
                except:
                    print("ERROR ASSIGNING VALUE")   
                index += 1    
            except:
                cont = False
        remove("./resetSounds.txt")
    except:
        print("ERROR")

main()
