import gspread
import time
from googleapiclient.discovery import build
from gspread.models import Worksheet
from oauth2client.service_account import ServiceAccountCredentials
from google.oauth2 import service_account

scope = ['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive.file', 'https://www.googleapis.com/auth/drive',]
creds = ServiceAccountCredentials.from_json_keyfile_name('key.json', scope)
client = gspread.authorize(creds)

gs = client.open_by_key("1H03M4vYkeq4-ktwMvCHj6t-q5m5CJPZqDd40YOZ8RiA").worksheet("engenharia_de_software")
i=4 
y=3

while gs.cell(i,y).value != "":
    time.sleep(7)
    media = (int(gs.cell(i,y+1).value) + int(gs.cell(i,y+2).value) + int(gs.cell(i,y+1).value))/3
    if(int(gs.cell(i,y).value) > 15):
        gs.update_cell(i,y+4, "Reprovado por falta")
        gs.update_cell(i, y+5, 0)
    else: 
        if(media<50):
            gs.update_cell(i, y+4, "Reprovado por nota")
            gs.update_cell(i, y+5, 0)
        if(media >=50 and media < 70):
            gs.update_cell(i, y+4, "Exame Final")

        if(media > 70):
            gs.update_cell(i, y+4, "Aprovado")
            gs.update_cell(i, y+5, 0)
    i=i+1

