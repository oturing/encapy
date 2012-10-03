class BulkItem(object):
    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        if value > 0:
            self.__weight = value
        else:
            raise ValueError('value must be > 0')
