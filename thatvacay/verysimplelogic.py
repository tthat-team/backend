from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

transactions = [
    {'From':"Julia", "To":"Sherry",'Amount':30}
]

balances = [
    {'Name': 'Julia', 'Balance': -50},
    {'Name': 'Sherry', 'Balance': 30},
    {'Name': 'Addy', 'Balance': 20}
]

@app.route('/transactions')
def get_transactions():
    return jsonify(transactions) #send the array of JSON incomes back to users

@app.route('/balances')
def get_balances():
    return jsonify(balances)

@app.route('/transaction', methods=['POST'])
def add_transaction():
    newtransaction = request.get_json()
    transactions.append(newtransaction)
    #add transfer amt to first person balance and minus from second
    for i in range(len(balances)):
        if balances[i]["Name"] == newtransaction["From"]:
           balances[i].update("Balance"+= newtransaction["Amount"])

        if balances[i]["Name"] == newtransaction["To"]:
           balances[i].update("Balance"-= newtransaction["Amount"])

    return '', 204

    
app.run(debug = True, port = 8080)