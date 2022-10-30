from marshmallow import post_load

from .transaction import Transaction, TransactionSchema
from .transaction_type import TransactionType


class Transfer(Transaction): #this class hardcodes the type of transaction
    def __init__(self, creditor, debtor, amount):
        super().__init__(creditor, debtor, amount, TransactionType.TRANSFER)

    #def __repr__(self):
    #    return '<Income(name={self.description!r})>'.format(self=self)#format(value_to_change=value_passed)


class TransferSchema(TransactionSchema):
    @post_load
    def make_transfer(self, data, **kwargs):
        return Transfer(**data)