from winreg import *

def findLocations():
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
                print(EnumValue(rawKey3,0))
            except:
                print("error")
            index += 1
        except:
            cont = False
            print("sdkjhf")

        print("\n")

findLocations()

