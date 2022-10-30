from flask import Flask, jsonify, request

from thatvacay.model.spending import Spending, SpendingSchema
from thatvacay.model.transfer import Transfer, Transferchema
from thatvacay.model.transaction_type import TransactionType

app = Flask(__name__)



transactions = [ #list of Expenses and Incomes
    Transfer("Addy", "Julia", 10)
    Spending("Julia", "Sherry", 30)
    
]


@app.route('/transfers')
def get_transfers():
    schema = TransferSchema(many=True) #IncomeSchema produces a JSON representation of incomes
    transfers = schema.dump(
        filter(lambda t: t.type == TransactionType.TRANSFER, transactions) #extract incomes only from the transactions list
    )
    return jsonify(transfers) #send the array of JSON incomes back to users


@app.route('/transfers', methods=['POST'])
def add_transfer():
    transfer = TransferSchema().load(request.get_json()) #load an instance of Income based on the JSON data sent by the user
    transactions.append(transfer) #added the new Income in transactions list
    return "", 204
    

#these are almost the same as the income ones
@app.route('/spendings')
def get_spendings():
    schema = SpendingSchema(many=True)
    spendings = schema.dump(
        filter(lambda t: t.type == TransactionType.SPENDING, transactions)
    )
    return jsonify(spendings)


@app.route('/spendings', methods=['POST'])
def add_spending():
    spending = SpendingSchema().load(request.get_json())
    transactions.append(spending)
    return "", 204


if __name__ == "__main__":
    app.run()