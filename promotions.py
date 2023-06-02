from abc import ABC


class Promotion(ABC):
    def __init__(self, name):
        self.name = name

    def apply_promotion(self, product, quantity):
        pass


class SecondHalfPrice(Promotion):
    def __init__(self, name):
        self.name = name

    def apply_promotion(self, product, quantity):
        return (product.price * quantity) / 2


class ThirdOneFree(Promotion):
    def __init__(self, name):
        self.name = name

    def apply_promotion(self, product, quantity):
        return ((product.price * quantity) / 3) * 2


class PercentDiscount(Promotion):
    def __init__(self, name, percent):
        self.name = name
        self.percent = percent

    def apply_promotion(self, product, quantity):
        percentage_discount = (100 - self.percent) / 100
        return product.price * percentage_discount
