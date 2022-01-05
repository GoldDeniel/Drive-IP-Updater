import time
import os
import pip

if os.name == 'nt':
    clear = lambda: os.system('cls')
else:
    clear = lambda: os.system('clear')
    
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

from requests import get
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from requests.sessions import extract_cookies_to_jar

os.chdir('../credentials')
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)
os.chdir('../data')
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
                UpdateIP.UpdateFileContent(file1)
        return
    
    def UpdateFileContent(file1):
        global externalIPAddress
        if externalIPAddress != file1.GetContentString():
            print('The ip does not match. Trying to set the content to the global ip in string.')

            file1.SetContentString(externalIPAddress) # Set content of the file from given string.
            file1.Upload()
        else:

            print('The ip matches. Sleeping for 300 seconds')
            time.sleep(300)

     
    
  
while True:
    UpdateIP.DriveRootFolderQuery()
