class Flower:

    def __init__(self, name=None, petals=None, price=None):
        self.name = self.petals = self.price = None

        self.set_name(name)
        self.set_petals(petals)
        self.set_price(price)

    def set_name(self, name):
        try:
            self.name = str(name)
        except ValueError and TypeError:
            print('Invalid input for a name, it must be a string.')

    def set_petals(self, petals):
        try:
            self.petals = int(petals)
        except ValueError and TypeError:
            print('Invalid input for petals, it must be a integer.')

    def set_price(self, price):
        try:
            self.price = float(price)
        except ValueError and TypeError:
            print('invalid input for price, it must be a number.')

    def get_name(self):
        if self.name is None or self.name == 'None':
            return 'Attribute has not been set.'
        else:
            return self.name

    def get_petals(self):
        if self.petals is None:
            return 'Attribute has not been set.'
        else:
            return self.petals

    def get_price(self):
        if self.price is None:
            return 'Attribute has not been set.'
        else:
            return self.price


if __name__ == '__main__':
    A = Flower('dandelion', '50', 10.32)
    print(A.get_name(), A.get_petals(), A.get_price())

    print('\n')
    Rose = Flower()
    print(Rose.get_name(), Rose.get_petals(), Rose.get_price())
    Rose.set_name('rose')
    Rose.set_petals(15)
    Rose.set_price(10.5)
    print(Rose.get_name(), Rose.get_petals(), Rose.get_price())
