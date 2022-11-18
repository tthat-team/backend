from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

transactions = [
    {'From':"Julia", "To":"Sherry",'Amount':30}
]

balance = [
    {'Name': 'Julia', 'Balance': -50},
    {'Name': 'Sherry', 'Balance': 30},
    {'Name': 'Addy', 'Balance': 20}
]

@app.route('/transactions')
def get_transactions():
    return jsonify(transactions) #send the array of JSON incomes back to users


@app.route('/transactions', methods=['POST'])
def add_transaction():
    transactions.append(request.get_json())
    return '', 204



    
app.run(debug = True, port = 8080)