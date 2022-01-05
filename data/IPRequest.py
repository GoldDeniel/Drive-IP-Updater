import pip
import os
import ctypes
ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 0 )
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
#import ctypes
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from requests import get
from requests.sessions import extract_cookies_to_jar



externalIPAddress = ''
class UpdateIP:
    def DriveRootFolderQuery():
        global externalIPAddress
        os.chdir('../credentials')
        gauth = GoogleAuth()
        gauth.LocalWebserverAuth()
        drive = GoogleDrive(gauth)
        os.chdir('../data')

        file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
        for file1 in file_list:
            if  'IPUpdate.txt' in file1['title']:
                externalIPAddress = file1.GetContentString()
                clear()
                try:
                    pyperclip.copy(externalIPAddress)
                except:
                    print('Could not copy to clipboard')
                file2 = open("external_ip.txt", "w")
                file2.write(externalIPAddress)
                
                
        return
    
UpdateIP.DriveRootFolderQuery()
# # # if os.name=='nt':
    # # # ctypes.windll.user32.messageboxw(0, 'ip was copied to the clipboard, and \'external_ip.txt\' was generated!', externalipaddress, 1)
                
