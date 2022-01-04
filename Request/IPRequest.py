import pip
import os
clear = lambda: os.system('cls')

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

import pyperclip
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
        #print('externalip in DriveRootFolderQuery is')
        #print(externalIPAddress)
        externalIPAddress = get('https://api.ipify.org').text
        file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
        for file1 in file_list:
            if  'IPUpdate.txt' in file1['title']:
                #print('title: %s, id: %s' % (file1['title'], file1['id']))
                clear()
                print('Current IP is ' + file1.GetContentString() + ' that was copied to the clipboard!')
                pyperclip.copy(file1.GetContentString())
        return

UpdateIP.DriveRootFolderQuery()
