import gspread
import math
import time
from oauth2client.service_account import ServiceAccountCredentials

#Hello Tunts team, this is my Tunts Challenge submission in python.

#Connection with Google Sheets API
scope = ['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive.file', 'https://www.googleapis.com/auth/drive',]
creds = ServiceAccountCredentials.from_json_keyfile_name('key.json', scope)
client = gspread.authorize(creds)
#Connecting with the Sheet "engenharia_de_software", so everytime you need to access the sheet, you must use the gs variable
gs = client.open_by_key("1H03M4vYkeq4-ktwMvCHj6t-q5m5CJPZqDd40YOZ8RiA").worksheet("engenharia_de_software")

def main():
    i=4; y=3
    abscence = 25/100 * 60

    #Loop through all the rows in the sheet
    while gs.cell(i,y).value != "":

        student = gs.cell(i,y-1).value
        p1 = int(gs.cell(i,y+1).value)
        p2 = int(gs.cell(i,y+2).value)
        p3 = int(gs.cell(i,y+3).value)

        #Since the google api has a limit of request per minute per user, its necessary to delay the application
        time.sleep(7)

        avg = (p1+p2+p3)/3

        #Verify the abscense of the student
        if(int(gs.cell(i,y).value) > abscence):
            gs.update_cell(i,y+4, "Reprovado por falta")
            gs.update_cell(i, y+5, 0)
            print("Aluno: " + student + " Reprovado por falta")
        else: 
            #Verify the average of the student and set if he/she failed(<50), needs final exam(50-70), or is approved(>70) in the course
            if(avg<50):
                gs.update_cell(i, y+4, "Reprovado por nota")
                gs.update_cell(i, y+5, 0)
                print("Aluno: " + student + " Reprovado por nota")
            if(avg >=50 and avg < 70):
                gs.update_cell(i, y+4, "Exame Final")
                #Since its not at my disposal the value of the final exam, i supposed that the NAF is what the student need to get approved
                gs.update_cell(i, y+5, math.ceil((100 - avg)))
                print("Aluno: " + student + " precisa de " +str(math.ceil(100-avg)) + " para ser aprovado")
            if(avg > 70):
                gs.update_cell(i, y+4, "Aprovado")
                gs.update_cell(i, y+5, 0)
                print("Aluno: " + student + " Aprovado por nota")
        i=i+1

if __name__ == '__main__':
    main()