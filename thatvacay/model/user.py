from marshmallow import Schema, fields

class User(object):
    def init(self, name, balance):
        self.name=name
        self.balance=balance

def get_state(self):
    if balance < 0:
        return 'You owe ppl' 
    elif balance == 0:
        return 'yay'    
    if balance > 0:
        return 'ppl owe u'

def get_balance(self):
    return self.balance


class UserSchema(Schema): #deserialize and serialize instances of Transaction from and to JSON objects
    name = fields.Str()
    balance = fields.Number()