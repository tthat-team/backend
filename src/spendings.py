def update_balances_spending(balances,transactor, totalCost): #split the costs of a transfer with everyone in the group
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
    
    if len(balances) == 1:
        balances[0]["Balance"] = 0 
    
    return balances