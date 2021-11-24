class CreditCard:
    __slots__ = '_customer', '_bank', '_account', '_balance', '_limit'

    def __init__(self, customer, bank, account, limit, balance=0):
        self._customer = customer
        self._bank = bank
        self._account = account
        self._limit = limit
        self._balance = balance

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
    card1 = CreditCard('Andy', 'standard bank', '7421 2350 1681 8949', 1000)
    card1.make_payment(100)
    print(card1.get_balance())
    card2 = CreditCard('Bella', 'business bank', '1465 6816 1688 3188', 2000, 500)
    card2.make_payment(1000)
    print(card2.get_balance())
