class CreditCard:

    __slots__ = '_customer', '_bank', '_account', '_balance', '_limit'

    def __init__(self, customer, bank, account, limit):
        self._customer = customer
        self._bank = bank
        self._account = account
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        return self._customer

    def get_bank(self):
        return self._bank

    def get_account(self):
        return self._account

    def get_limit(self):
        return self._limit

    def get_balance(self):
        return self._balance

    def charge(self, price):
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        self._balance -= amount


class PredatoryCreditCard(CreditCard):

    __slots__ = '_apr', '_num_charge'
    OverLimit_Fee = 5
    Max_Charge = 10

    def __init__(self, customer, bank, account, limit, apr):
        super().__init__(customer, bank, account, limit)
        self._apr = apr
        self._num_charge = 0

    def charge(self, price):
        success = super().charge(price)
        if not success:
            self._balance += PredatoryCreditCard.OverLimit_Fee
        else:
            self._num_charge += 1
            if self._num_charge > PredatoryCreditCard.Max_Charge:
                self._balance += 1
        return success

    def process_month(self):
        if self._balance > 0:
            monthly_factor = pow(1 + self._apr, 1 / 12)
            self._balance *= monthly_factor
        self._num_charge = 0
