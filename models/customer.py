class Customer:
    all_ustomers= []


    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        Customer.all_customers.append(self)

    @property
    def given_name(self):
        return self._given_name

    @given_name.setter
    def name(self, new_name):
        self._given_name = new_name

    @property
    def family_name(self):
        return self._family_name

    @family_name.setter
    def family_name(self, new_family_name):
        self._family_name = new_family_name

    def full_name(self):
        return f"{self.given_name} {self.family_name}"

    @classmethod
    def all(cls):
        return cls.all_customers
