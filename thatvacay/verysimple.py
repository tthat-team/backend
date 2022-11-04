from flask import Flask, jsonify, request

app = Flask(__name__)


transactions = [
    {'Addy': 30, 'Julia': -50, 'Sherry' : 20}
]

@app.route('/transactions')
def get_transactions():
    return jsonify(transactions) #send the array of JSON incomes back to users


@app.route('/transactions', methods=['POST'])
def add_transaction():
    transactions.append(request.get_json())
    return '', 204
    
