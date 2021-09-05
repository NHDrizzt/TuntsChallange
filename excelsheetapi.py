from typing import ValuesView
from googleapiclient.discovery import build

from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'key.json'
SAMPLE_SPREADSHEET_ID = '1H03M4vYkeq4-ktwMvCHj6t-q5m5CJPZqDd40YOZ8RiA'

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

service = build('sheets', 'v4', credentials=creds)

# Call the GoogleSheet v4 API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="engenharia_de_software!A4:H27").execute()
values = result.get('values', [])
print(values)