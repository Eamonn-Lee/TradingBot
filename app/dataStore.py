import json

class Transaction:
    def __init__(self, price, amount):
        self._price = price
        self._amount = amount

    def verify(self):
        # How to verify data is ok?
        # probably requires confirmation from broker site
        return True
    
    @property
    def amount(self):
        return self._amount

    def value(self):
        return (self._price * self._amount)

class FinishedTransaction:
    # should be used as an archived record

    def __init__(self, buy, sold):
        if not isinstance(buy, Transaction) or not isinstance(sold, Transaction):
            raise TypeError(f"Expected a Transaction but received a {type(buy)} and {type(sold)} instead")
        self._buy = buy
        self._sold = sold
        self._remaining_amount = buy.amount - sold.amount
        self._initial_gen_value = sold.value() - buy.value()

    @property
    def remaining_amount(self):
        return self._remaining_amount
    
    @property
    def initial_value(self):
        return self._initial_gen_value
        
t1 = Transaction(10, 3)
t2 = Transaction(30, 1)

fin = FinishedTransaction(t1, t2)
print(fin.remaining_amount)
print(fin._initial_gen_value)