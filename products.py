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
        except (TypeError, NameError) as e:
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

    def get_quantity(self):

        if self.quantity > 0:
            self.activate()

        return float(self.quantity)

    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()
        self.activate()

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        return f"{self.name}, Price : {self.price}, Quantity : {self.quantity}"

    def buy(self, quantity):
        total = float(quantity) * self.price
        try:
            if self.quantity - quantity < 0:
                raise ValueError
            self.quantity -= quantity
            self.set_quantity(self.quantity)
            return total
        except ValueError as e:
            # or if self.quantity - quantity < 0: return "not enough stock available to facilitate order" without try/except
            print(f"not enough stock available to facilitate order, Quantity : {self.quantity}")


