import os

# pylint: disable=locally-disabled, multiple-statements, fixme, line-too-long, maybe-no-member
from flask import Flask

from googleapiclient.discovery import build
from google.oauth2 import service_account
from datetime import datetime

data = "helloworld/keys.json"

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = data 
credentials = None
credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# If modifying these scopes, delete the file token.json.

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1oYuQw70RS_Fqio890OV3ff6cDeAQRPkRHsm5ul0NRG0'
service = build('sheets', 'v4', credentials=credentials)

# Call the Sheets API
sheet = service.spreadsheets()

app = Flask(__name__)

@app.route("/")
def hello_world():
    
    now = datetime.now()
    year = now.strftime("%Y")
    month = now.strftime("%m")
    day = now.strftime("%d")
    time=now.strftime("%H:%M:%S")
    values = [[year],[month],[day],[time]]
    body = {
        'values': values
    }
    result = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="A1",valueInputOption="USER_ENTERED", body=body).execute()
    return time


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=int(os.environ.get("PORT", 8080)))

