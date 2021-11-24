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


if __name__ == '__main__':
    wallet = [CreditCard('John Bowman', 'California Saving', '5391 0375 9387 5309', 2500),
              CreditCard('John Bowman', 'California Federal', '3485 0399 3395 1954', 3500),
              CreditCard('John Bowman', 'California Finance', '5391 0375 9387 5309', 5000)]

    for val in range(1, 100):
        if wallet[0].charge(val) is False:
            print(val)
            break
    for val in range(1, 100):
        if wallet[1].charge(2*val) is False:
            print(val)
            break
    for val in range(1, 100):
        if wallet[2].charge(3*val) is False:
            print(val)
            break
