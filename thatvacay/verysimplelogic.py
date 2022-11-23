from flask import Flask, jsonify, request
from flask_cors import CORS
from operator import itemgetter

app = Flask(__name__)
CORS(app)

transfers = [
    #{'From':"Julia", "To":"Sherry",'Amount':30}
]

balances = [
   # {'Name': 'Julia', 'Balance': 50},
   # {'Name': 'Sherry', 'Balance': -30},
   # {'Name': 'Addy', 'Balance': -20}
]

optimized_routes = [
    #{'From':"Julia", "To":"Sherry",'Amount':30}
]

spendings = [
    #{"Name":"Pooo", "Amount":30}
]

transactions = [ #combo of spendings and transfers

]


@app.route('/users')
def get_users():
    users = []
    for i in range(len(balances)):
        users.append(balances[i]["Name"])
    return jsonify(users)

@app.route('/users', methods=['POST'])
def add_user():
    new_user = request.get_json()
    balances.append({'Name': new_user, 'Balance': 0})
    return '', 203


@app.route('/transactions')
def get_transactions():
    return jsonify(transactions)



@app.route('/transfers')
def get_transfers():
    return jsonify(transfers) #send the array of JSON incomes back to frontend

@app.route('/transfers', methods=['POST'])
def add_transfer():
    new_transfer = request.get_json()
    transfers.append(new_transfer)
    transactions.append(new_transfer)
    update_balances_transfer(new_transfer)
    return '', 204



@app.route('/spendings', methods=['POST'])
def add_spending():
    new_spending= request.get_json()
    spendings.append(new_spending)
    transactions.append(new_spending)
    update_balances_spending(new_spending["Name"], new_spending["Amount"])
    return '', 205




@app.route('/balances')
def get_balances():
    return jsonify(balances)



@app.route('/optimizedroutes')
def get_optimizedroutes():
    optimize_route()
    return jsonify(optimized_routes)



def update_balances_transfer(newtransfer): #add transfer amt to first person balance and minus from second
    sender_exists = False
    receiver_exists = False
    for i in range(len(balances)):
        if balances[i]["Name"] == newtransfer["From"]:
            balances[i]["Balance"] = balances[i]["Balance"] + newtransfer["Amount"]
            sender_exists = True

        if balances[i]["Name"] == newtransfer["To"]:
            balances[i]["Balance"] = balances[i]["Balance"] - newtransfer["Amount"]
            receiver_exists = True

    if sender_exists == False: #theres def a better way to check if a value is in a dict
        balances.append({'Name': newtransfer["From"], 'Balance': newtransfer["Amount"]})

    if receiver_exists == False:
        balances.append({'Name': newtransfer["To"], 'Balance': -newtransfer["Amount"]})


# optimize_route() adds transfers with the format {'From': NAME1, "To": NAME2,'Amount': Num} to optimized_routes
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



def update_balances_spending(transactor, totalCost): #split the costs of a transfer with everyone in the group
    transactor_exists = False
    for i in range(len(balances)):
        if (balances[i]["Name"] == transactor): transactor_exists = True
    if transactor_exists == False:
        balances.append({'Name': transactor, 'Balance': 0}) 

    amtOwed = totalCost/(len(balances))

    for i in range(len(balances)):
        if (balances[i]["Name"] == transactor): # if the person is the transactor
            balances[i]["Balance"] = balances[i]["Balance"] + (totalCost - amtOwed) #add to the amount owed less their own portion
        else: 
            balances[i]["Balance"] = balances[i]["Balance"] - amtOwed


app.run(debug = True, port = 8080)