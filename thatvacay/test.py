from operator import itemgetter

balances = [
    {
        "Balance": 33.33333333333333,
        "Name": "Julia"
    },
    {
        "Balance": -36.66666666666667,
        "Name": "Sherry"
    },
    {
        "Balance": 3.333333333333332,
        "Name": "Adeline"
    }
]

optimized_routes = [
    #{'From':"Julia", "To":"Sherry",'Amount':30}
]

def optimize_route(): 
    sorted_balances = sorted(balances, key=itemgetter("Balance"), reverse=True).copy()
    creditors = []
    debtors = []

    for i in range(len(sorted_balances)):
        if (sorted_balances[i]["Balance"])>0:
            creditors.append(sorted_balances[i])
        elif (sorted_balances[i]["Balance"])<0:
            debtors.append(sorted_balances[i])
    
    debtors = debtors[::-1]

    print("cred:",creditors,"debt:",debtors)

    i=0
    j=0
    #while i < min(len(creditors),len(debtors)) or j< min(len(creditors),len(debtors)):
    while i < len(creditors) and j < len(debtors):
        amount = min(creditors[i]["Balance"], abs(debtors[j]["Balance"]))
        new_route = 0
        if len(creditors) == len(debtors) == 1:
            new_route = {'From':debtors[j]["Name"], "To":creditors[i]["Name"],'Amount': 2*amount}
        else:
            new_route = {'From':debtors[j]["Name"], "To":creditors[i]["Name"],'Amount': amount}
        optimized_routes.append(new_route)

        debtors[j]["Balance"] += amount
        creditors[i]["Balance"] -= amount

        if debtors[j]["Balance"]  == 0: j+=1
        if creditors[i]["Balance"] == 0: i+=1

          #  if j=len(debtors) or i=len(creditors):
        #     optimized_routes.append({'From':debtors[j]["Name"], "To":creditors[i]["Name"],'Amount': amount})

optimize_route()
print("routes:",optimized_routes)