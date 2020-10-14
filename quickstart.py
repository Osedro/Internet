from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication.

drive = GoogleDrive(gauth)
'''
fileList = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
for file in fileList:
  print('Title: %s, ID: %s' % (file['title'], file['id']))
  # Get the folder ID that you want
  if(file['title'] == "teste"):
      fileID = file['id']
'''
file1 = drive.CreateFile({'title': 'Hello.txt', "parents": [{"kind": "drive#fileLink", "id": '1J4bGOObOfAEv2BJmiZLVycvuWCnTNPAd'}]})  # Create GoogleDriveFile instance with title 'Hello.txt'.
file1.SetContentString('Hello World!') # Set content of the file from given string.
file1.Upload()
