from flask import Flask, request
import  os
from dotenv import load_dotenv
from utils import topup

load_dotenv()

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

@app.route('/')
def main():
    return "Hello world!"

@app.route('/transfer/airtime', methods=['POST'])
def transfer_airtime():
    data = request.get_json()
    if not data.get('amount') or type(data.get('amount')) != int:
        return "Amount is required and should be an integer", 400
    if not data.get('phone_number') or len(data.get('phone_number')) != 11:
        return "Phone number is required and must be valid e.g 09011233312", 400
    if not data.get('sender_phone_number') or len(data.get('sender_phone_number')) != 11:
        return "Sender phone number is required  and must be valid e.g 09011233312", 400
    try:
        data = topup(data['amount'], data['phone_number'], data['sender_phone_number'])
        return data, 200
    except Exception as e:
        return str(e), 400

if __name__ == '__main__':
    app.run(debug=True)