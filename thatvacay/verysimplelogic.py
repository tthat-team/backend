from flask import Flask, jsonify, request
from flask_cors import CORS
from operator import itemgetter

app = Flask(__name__)
CORS(app)

transactions = [
    #{'From':"Julia", "To":"Sherry",'Amount':30}
]

balances = [
    {'Name': 'Julia', 'Balance': 50},
    {'Name': 'Sherry', 'Balance': -30},
    {'Name': 'Addy', 'Balance': -20}
]

optimized_routes = [
    #{'From':"Julia", "To":"Sherry",'Amount':30}
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
    calculate_balances(newtransaction)
    return '', 204

@app.route('/optimizedroutes')
def get_optimizedroutes():
    optimize_route()
    return jsonify(optimized_routes)

def calculate_balances(newtransaction): #add transfer amt to first person balance and minus from second
    sender_exists = False
    receiver_exists = False
    for i in range(len(balances)):
        if balances[i]["Name"] == newtransaction["From"]:
            balances[i]["Balance"] = balances[i]["Balance"] + newtransaction["Amount"]
            sender_exists = True

        if balances[i]["Name"] == newtransaction["To"]:
            balances[i]["Balance"] = balances[i]["Balance"] - newtransaction["Amount"]
            receiver_exists = True

    if sender_exists == False: #theres def a better way to check if a value is in a dict
        balances.append({'Name': newtransaction["From"], 'Balance': newtransaction["Amount"]})

    if receiver_exists == False:
        balances.append({'Name': newtransaction["To"], 'Balance': -newtransaction["Amount"]})

def optimize_route():
    sorted_balances = sorted(balances, key=itemgetter("Balance"), reverse=True)
    creditors = []
    debtors = []

    for i in range(len(sorted_balances)):
        if (sorted_balances[i]["Balance"])>0:
            creditors.append(sorted_balances[i])
        elif (sorted_balances[i]["Balance"])<0:
            debtors.append(sorted_balances[i])
    
    debtors = debtors[::-1]

    i=0
    j=0
    while i < min(len(creditors),len(debtors)) or j< min(len(creditors),len(debtors)):
        amount = min(creditors[i]["Balance"], abs(debtors[j]["Balance"]))
        new_route = {'From':debtors[j]["Name"], "To":creditors[i]["Name"],'Amount': amount}
        optimized_routes.append(new_route)

        debtors[j]["Balance"] += amount
        creditors[i]["Balance"] -= amount

        if debtors[j]["Balance"]  == 0: j+=1
        if creditors[i]["Balance"] == 0: i+=1


app.run(debug = True, port = 8080)