

def update_balances_transfer(balances, newtransfer): #add transfer amt to first person balance and minus from second
    sender_exists = False
    receiver_exists = False
    for i in range(len(balances)):
        if balances[i]["Name"] == newtransfer["From"]:
            balances[i]["Balance"] = balances[i]["Balance"] + float(newtransfer["Amount"])
            sender_exists = True

        if balances[i]["Name"] == newtransfer["To"]:
            balances[i]["Balance"] = balances[i]["Balance"] - float(newtransfer["Amount"])
            receiver_exists = True

    if sender_exists == False: #theres def a better way to check if a value is in a dict
        balances.append({'Name': newtransfer["From"], 'Balance': float(newtransfer["Amount"])})

    if receiver_exists == False:
        balances.append({'Name': newtransfer["To"], 'Balance': - float(newtransfer["Amount"])})

    return balances