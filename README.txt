AUTO CONNECT TO REMOTE DESKTOP

This script doesn't connect automatically yet, but requests the ip address and starts mstsc.exe (RDP) on MS machines.

REQUEST

Simply requests the IP from the root folder of your google drive.

UPDATER

The script keeps updating the txt on the cloud that's being used to request the remote IP.

HOW TO USE IT:

First, you need to setup pydrive:

- Go to APIs Console ( https://console.cloud.google.com/iam-admin/projects ) and make your own project.
- Search for ‘Google Drive API’, select the entry, and click ‘Enable’.
- Select ‘Credentials’ from the left menu, click ‘Create Credentials’, select ‘OAuth client ID’.
- Now, the product name and consent screen need to be set -> click ‘Configure consent screen’ and follow the instructions. 

Once finished:

- Select ‘Application type’ to be Web application.
- Enter an appropriate name.
- Input http://localhost:8080 for ‘Authorized JavaScript origins’.
- Input http://localhost:8080/ for ‘Authorized redirect URIs’.
- Click ‘Save’.
- Click ‘Download JSON’ on the right side of Client ID to download client_secret_<really long ID>.json.

The downloaded file has all authentication information of your application.
Rename the file to “client_secrets.json” and place it in the ‘credentials’ folder (overwrite the old one).
Very bad and probably very much not accurate templates are already in the folders to help you understand better
what you have to do but honestly I don't know either.

You can find the official documentation that probably provides more help here: https://pythonhosted.org/PyDrive/
