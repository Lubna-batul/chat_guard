import os
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request

SCOPE=["https://www.googleapis.com/auth/gmail.modify"]
creds=None
if os.path.exists("token.json"):
    creds=Credentials.from_authorized_user_file("token.json",SCOPE)
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow=InstalledAppFlow.from_client_secrets_file("credentials.json",SCOPE)
        creds=flow.run_local_server(port=0)
    
    with open("token.json","w")as token:
        token.write(creds.to_json())
print("Authentication successful!")

