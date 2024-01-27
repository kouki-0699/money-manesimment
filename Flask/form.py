from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('maney.html')

#gsspread_api_infomation
import gspread  
from oauth2client.service_account import ServiceAccountCredentials
sp_credential_file ='C:\Users\kouki.KOUKI\money-manesimment\Flask\money-manesimment api_infomation.json'
sp_scope =["https://spreadsheets.google.com/feeds", 
           "https://www.googleapis.com/auth/spreadsheets",
           "https://www.googleapis.com/auth/drive.file", 
           "https://www.googleapis.com/auth/drive"]
sp_sheet_id ="1vwloBGidR-Mr8-Y8YiQfa1Y_ycMFfS89yi9kFLU2WlQ"
sp_sheet_name =["January",]  #後で変更（シートネーム　月ごと（英語））

credentials = ServiceAccountCredentials.from_json_keyfile_name(sp_credential_file, sp_scope)
gc = gspread.authorize(credentials)

sh = gc.open_by_key(sp_sheet_id)
worksheet_January= sh.worksheet(sp_sheet_name)


#処理
@app.route('/process_data', methods=['POST'])
def process_data():
    month = request.form['month']
    date =request.form['date']  
    income = request.form['income']
    expenses = request.form['expenses']
    free_text = request.form['free_text']
    
    worksheet_January.append_row([month,date,])#列に表示させる内容
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
