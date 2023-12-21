class Review:
    all_reviews= []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        Review.all_reviews.append(self)

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, new_rating):
        if not isinstance(new_rating, (int, float)):
            raise ValueError("Rating must be a number.")
        if not (0 <= new_rating <= 10):
            raise ValueError("Rating must be a value between 0 and 10.")
        self._rating = new_rating

    @classmethod
    def all(cls):
        return cls.all_reviews