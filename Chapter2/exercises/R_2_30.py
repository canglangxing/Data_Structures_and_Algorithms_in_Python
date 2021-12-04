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

    def _set_balance(self, value):
        self._balance = value


class PredatoryCreditCard(CreditCard):

    __slots__ = '_apr'
    OverLimit_Fee = 5

    def __init__(self, customer, bank, account, limit, apr):
        super().__init__(customer, bank, account, limit)
        self._apr = apr

    def charge(self, price):
        success = super().charge(price)
        if not success:
            super()._set_balance(super().get_balance() + PredatoryCreditCard.OverLimit_Fee)
        return success

    def process_month(self):
        if super().get_balance() > 0:
            monthly_factor = pow(1 + self._apr, 1 / 12)
            super()._set_balance(super().get_balance() * monthly_factor)
