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
        try:
            price = float(price)
        except BaseException:
            print('Invalid input')
            return False
        else:
            if price + self._balance > self._limit:
                return False
            else:
                self._balance += price
                return True

    def make_payment(self, amount):
        try:
            amount = float(amount)
        except BaseException:
            print('Invalid input')
            return False
        else:
            if amount < 0:
                raise ValueError("payment can't be negative.")
            else:
                self._balance -= amount
                return True
