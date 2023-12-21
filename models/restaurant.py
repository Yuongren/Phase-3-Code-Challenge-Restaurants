class Restaurant:
    all_restaurants = []
    def __init__(self, name):
        self.name = name
        Restaurant.all_restaurants.append(self)

    @property
    def name(self):
        return self.name