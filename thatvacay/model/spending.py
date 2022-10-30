from marshmallow import post_load

from .transaction import Transaction, TransactionSchema
from .transaction_type import TransactionType


class Spending(Transaction):
    def __init__(self, creditor, debtor, amount):
        super().__init__(creditor, debtor, amount, TransactionType.SPENDING)
        #self.description=description
    #def __repr__(self):
      #  return '<Expense(name={self.description!r})>'.format(self=self)


class SpendingSchema(TransactionSchema):
    @post_load
    def make_spending(self, data, **kwargs):
        return Spending(**data)