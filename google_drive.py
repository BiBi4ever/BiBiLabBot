from bot inport ID

def authorization (ID):
  SCOPES = ['https://www.googleapis.com/auth/drive']
  credentials = ServiceAccountCredentials.from_json_keyfile_dict(
       ID, scopes=SCOPES)
  service = build('drive', 'v3', credentials=credentials)
  return service
