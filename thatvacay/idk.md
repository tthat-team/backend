
Transaction (creditor, debtor, amount, type) ––––> User(name, balance) 
         ^                          ^
        /                            \
Transfer (creditor, debtor,      Spending (creditor, debtor,
description, amount)             amount) type=spending
type=transfer

