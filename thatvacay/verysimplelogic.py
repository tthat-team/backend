from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

transactions = [
    #{'From':"Julia", "To":"Sherry",'Amount':30}
]

balances = [
    {'Name': 'Julia', 'Balance': 0},
    {'Name': 'Sherry', 'Balance': 0},
    {'Name': 'Addy', 'Balance': 0}
]

optimized_routes = [
    
]



@app.route('/transactions')
def get_transactions():
    return jsonify(transactions) #send the array of JSON incomes back to users

@app.route('/balances')
def get_balances():
    return jsonify(balances)

@app.route('/transactions', methods=['POST'])
def add_transaction():
    newtransaction = request.get_json()
    transactions.append(newtransaction)
    #add transfer amt to first person balance and minus from second
    sender_exists = False
    receiver_exists = False

    for i in range(len(balances)):
        if balances[i]["Name"] == newtransaction["From"]:
            balances[i]["Balance"] = balances[i]["Balance"] + newtransaction["Amount"]
            sender_exists = True

        if balances[i]["Name"] == newtransaction["To"]:
            balances[i]["Balance"] = balances[i]["Balance"] - newtransaction["Amount"]
            receiver_exists = True

    if sender_exists == False:
        balances.append({'Name': newtransaction["From"], 'Balance': newtransaction["Amount"]})

    if receiver_exists == False:
        balances.append({'Name': newtransaction["To"], 'Balance': -newtransaction["Amount"]})

    return '', 204
    
app.run(debug = True, port = 8080)