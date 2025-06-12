
from flask import Flask, jsonify
from smartapi import SmartConnect
import pyotp

app = Flask(__name__)

API_KEY = "609mA1G8"
CLIENT_ID = "V53432609"
PASSWORD = "V!k@$#&Angel01"
TOTP_SECRET = "M7AUEWK53J3M2QBM5UWZVTLWTE"

client = SmartConnect(api_key=API_KEY)

def get_token():
    otp = pyotp.TOTP(TOTP_SECRET).now()
    session = client.generateSession(CLIENT_ID, PASSWORD, otp)
    return session['data']['refreshToken']

@app.route("/price/<symbol>")
def get_price(symbol):
    get_token()
    ltp_data = client.ltpData("NSE", symbol.upper())
    return jsonify({ "ltp": ltp_data["data"]["ltp"] })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
