import pip
import os
def clear():
    os.system('cls' if os.name=='nt' else 'clear')
clear()
def import_or_install():
    try:
        from pydrive.auth import GoogleAuth
        from pydrive.drive import GoogleDrive
        import pyperclip
    except ImportError:
        pip.main(['install', 'pydrive']) 
        pip.main(['install', 'pyperclip']) 
        
        clear()
        print('pydrive has been installed!')
import_or_install()

import time
import pyperclip
import ctypes
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from requests import get
from requests.sessions import extract_cookies_to_jar


gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)
externalIPAddress = ''
class UpdateIP:
    def DriveRootFolderQuery():
        global externalIPAddress

        file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
        for file1 in file_list:
            if  'IPUpdate.txt' in file1['title']:
                externalIPAddress = file1.GetContentString()
                clear()
                pyperclip.copy(externalIPAddress)
                
                file2 = open("external_ip.txt", "w")
                file2.write(externalIPAddress)
                
                if os.name=='nt':
                    ctypes.windll.user32.MessageBoxW(0, 'IP was copied to the clipboard, and \'external_ip.txt\' was generated!', externalIPAddress, 1)
                
        return
    
UpdateIP.DriveRootFolderQuery()
