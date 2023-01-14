from operator import itemgetter

# optimize_route() adds transfers with the format {'From': NAME1, "To": NAME2,'Amount': Num} to optimized_routes
def optimize_route(balances): 
    optimized_routes = []
    copy_balances = [{'Name': x["Name"], 'Balance': x["Balance"]} for x in balances]
    sorted_balances = sorted(copy_balances, key=itemgetter("Balance"), reverse=True)
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
    while i < len(creditors) and j < len(debtors):
        amount = min(creditors[i]["Balance"], abs(debtors[j]["Balance"]))
        new_route = {'From':debtors[j]["Name"], "To":creditors[i]["Name"],'Amount': amount}
        optimized_routes.append(new_route)

        debtors[j]["Balance"] += amount
        creditors[i]["Balance"] -= amount

        if debtors[j]["Balance"]  == 0: j+=1
        if creditors[i]["Balance"] == 0: i+=1

    return optimized_routes

