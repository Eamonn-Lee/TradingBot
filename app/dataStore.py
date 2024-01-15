import json

class Transaction:
    def __init__(self, price, amount):
        self.price = price
        self.amount = amount

    def verify(self):
        # How to verify data is ok?
        # probably requires confirmation from broker site
        return True

    def value(self):
        return (self.price * self.amount)

class FinishedTransaction:
    def __init__(self, buy, sold):
        if not isinstance(buy, Transaction) or not isinstance(sold, Transaction):
            raise TypeError(f"Expected a Transaction but received a {type(buy)} and {type(sold)} instead")
        self.buy = buy
        self.sold = sold

    def value(self):

        

        
tran1 = Transaction(10, 3)
print(tran1.value())