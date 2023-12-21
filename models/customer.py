class Customer:
    all = []


    def __init__(self, name, restaurant):
        self.name = name
        self.restaurant = restaurant
        Customer.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self.name = name

    @property
    def restaurant(self):
        self.restaurant

    @classmethod
    def all(cls):
        return cls.all
