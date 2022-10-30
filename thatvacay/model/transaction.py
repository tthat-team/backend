import datetime as dt

from marshmallow import Schema, fields


class Transaction(object): #subclass of object
    def __init__(self, creditor, debtor, amount, type):
        self.creditor = creditor#.getname()
        self.debtor = debtor
        self.amount = amount
        self.created_at = dt.datetime.now()
        self.type = type

    #def __repr__(self):
   #     return '<Transaction(name={self.description!r})>'.format(self=self)


class TransactionSchema(Schema): #deserialize and serialize instances of Transaction from and to JSON objects
    creditor = fields.Str()
    debtor = fields.Str()
    amount = fields.Number()
    created_at = fields.Date()
    type = fields.Str()

