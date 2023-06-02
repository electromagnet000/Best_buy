import promotions


class Product:

    # set the parameters for Product
    def __init__(self, name=None, price=None, quantity=None):
        # if the product has a parameter missing then it will tell the person while running other codes
        super().__init__()
        # tries to get correct data for the parameters
        try:
            if name == "" or name is None:
                raise TypeError
            self.name = str(name)
        except (TypeError, NameError, AttributeError) as e:
            print(f"there was a problem with name, please check if there is a name : {e}")

        try:
            if price < 0 or price is None:
                raise ValueError
            self.price = price
        except (TypeError, ValueError) as e:
            print(f"there was a problem with price, Please check if it's a positive integer: {e}, Price : {price}")

        try:
            if quantity < 0 or quantity is None:
                raise ValueError
            self.quantity = quantity
        except (TypeError, ValueError) as e:
            print(
                f"there was a problem with quantity, Please check if it's a positive integer: {e}, Quantity :  {quantity}")

        self.active = None
        self.NonStockedProduct = False
        self.LimitedProduct = False
        self.promotion = None


    def get_quantity(self):

        if self.quantity <= 0:
            self.deactivate()
        elif self.quantity > 0:
            self.activate()

        return float(self.quantity)

    def get_promotion(self):
        return self.promotion

    def set_quantity(self, quantity):
        self.quantity = quantity

        if self.quantity == 0:
            self.deactivate()
        elif self.quantity > 0:
            self.activate()

    def set_promotion(self, promotion):
        self.promotion = promotion

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        if self.promotion:
            return f"{self.name}, Price : {self.price}, Quantity : {self.quantity} Promotions on item : {self.promotion.name}"
        return f"{self.name}, Price : {self.price}, Quantity : {self.quantity} Promotions on item : {self.promotion}"
    def buy(self, quantity):
        total = float(quantity) * self.price
        try:
            if self.LimitedProduct:
                check_if_over_maximum = self.maximum
                if quantity > check_if_over_maximum:
                    print(f"order above maximum per order : {self.maximum}")
                    return 0
            elif self.NonStockedProduct:
                return total
            elif self.quantity - quantity < 0:
                raise ValueError

            if self.promotion:
                if self.promotion == promotions.SecondHalfPrice(""):
                    if quantity % 2 == 0:
                        total = self.promotion.apply_promotion(self, quantity)
                elif self.promotion == promotions.PercentDiscount("", 30):
                    total = self.promotion.apply_promotion(self, 30)
                else:
                    if quantity >= 3:
                        total = self.promotion.apply_promotion(self, quantity)

            self.quantity -= quantity
            self.set_quantity(self.quantity)
            return total

        except ValueError as e:
            # or if self.quantity - quantity < 0: return "not enough stock available to facilitate order" without try/except
            print(f"not enough stock available to facilitate order, Quantity : {self.quantity}")


class NonStockedProduct(Product):
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.promotion = None
        self.quantity = 0
        self.NonStockedProduct = True
        self.LimitedProduct = False

    def show(self):
        return f"{self.name}, Price : {self.price} Promotion : {self.promotion.name}"


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.maximum = maximum
        self.LimitedProduct = True
        self.NonStockedProduct = False

    def show(self):
        return f"{self.name}, Price : {self.price}, Quanitity : {self.quantity}, Maximum per order : {self.maximum}  "
