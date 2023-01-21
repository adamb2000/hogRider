from winreg import *

def findLocations():
    registry = ConnectRegistry(None, HKEY_CURRENT_USER)
    rawKey = OpenKey(registry, "AppEvents\Schemes\Apps\.Default")
    cont = True
    index = 0

    while(cont):
        try:
            print(EnumKey(rawKey,index))
            index += 1
        except:
            cont = False
        

findLocations()