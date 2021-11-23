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
            self._balance -= amount
            return True


if __name__ == '__main__':
    card = CreditCard('Andy', 'standard bank', '7421 2350 1681 8949', 1000)
    card.make_payment(100)
    print(card.get_balance())
    card.make_payment('one hundred')
    print(card.get_balance())
    card.charge(500)
    print(card.get_balance())
    card.charge('one hundred')
    print(card.get_balance())
    card.charge(700)
    print(card.get_balance())
