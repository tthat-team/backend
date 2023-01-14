from flask import Flask, jsonify, request
from flask_cors import CORS
import optimize_routes as opt
import spendings as spd
import transfers as trans
import exchange as exc


app = Flask(__name__)
CORS(app)

transfers = [
    #{'From':"Julia", "To":"Sherry",'Amount':30}
]

balances = [
   {'Name': 'Julia', 'Balance': 50},
   {'Name': 'Sherry', 'Balance': -30},
   {'Name': 'Addy', 'Balance': -20}
]

spendings = [
    #{"Name":"Pooo", "Amount":30}
]

transactions = [ #combo of spendings and transfers

]

current_currency = ["CAD"]
userexists = False

@app.route('/users')
def get_users():
    users = []
    for i in range(len(balances)):
        users.append(balances[i]["Name"])
    return jsonify(users)

@app.route('/users', methods=['POST'])
def add_user():
    global userexists
    userexists = False
    new_user = request.get_json()
    for i in range(len(balances)): 
        if balances[i]["Name"] == new_user["Name"]:
            userexists = True 
    if userexists == False:
        balances.append({'Name': new_user["Name"], 'Balance': 0})
    return '', 203

@app.route('/addusererror')
def get_usererror():
    if userexists == False:
        return '', 203
    else:
        return jsonify("hi")

@app.route('/transactions')
def get_transactions():
    #rounded_trans = 
    return jsonify(transactions)

@app.route('/transfers')
def get_transfers():
    return jsonify(transfers) #send the array of JSON incomes back to frontend

@app.route('/transfers', methods=['POST'])
def add_transfer():
    new_transfer = request.get_json()
    transfers.append(new_transfer)
    transactions.append(new_transfer)
    trans.update_balances_transfer(balances,new_transfer)
    return '', 204

@app.route('/spendings')
def get_spendings():
    return jsonify(spendings) 
    
@app.route('/spendings', methods=['POST'])
def add_spending():
    new_spending = request.get_json()
    spendings.append(new_spending)
    transactions.append(new_spending)
    spd.update_balances_spending(balances, new_spending["Name"], float(new_spending["Amount"]))
    return '', 205

@app.route('/exchange', methods=['POST'])
def add_exchange_rate():
    new_currency = request.get_json()
    exc.change_global_currency(current_currency[0], new_currency["Currency"], balances)
    current_currency[0] = new_currency["Currency"]
    return '', 206

@app.route('/balances')
def get_balances():
    return jsonify(balances)

@app.route('/optimizedroutes')
def get_optimizedroutes():
    return jsonify(opt.optimize_route(balances))


app.run(debug = True, port = 8080)