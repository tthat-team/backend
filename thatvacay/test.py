from operator import itemgetter

balances = [
    {'Name': 'Julia', 'Balance': 50},
    {'Name': 'Sherry', 'Balance': -10},
    {'Name': 'Addy', 'Balance': 20},
    {'Name': 'Frank', 'Balance': -60}
]

optimized_routes = [
    #{'From':"Julia", "To":"Sherry",'Amount':30}
]

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

    for i in range(len(creditors)):
        for j in range(len(debtors)):
            amount = min(creditors[i]["Balance"],abs(debtors[j]["Balance"]))
            new_route = {'From':debtors[j]["Name"], "To":creditors[i]["Name"],'Amount': amount}
            optimized_routes.append(new_route)

            debtors[j]["Balance"] += amount
            creditors[i]["Balance"] -= amount

            if debtors[j]["Balance"] != 0: j-=1
            if creditors[i]["Balance"] != 0: i-=1

          #  if j=len(debtors) or i=len(creditors):
           #     optimized_routes.append({'From':debtors[j]["Name"], "To":creditors[i]["Name"],'Amount': amount})

optimize_route()
print(optimized_routes)