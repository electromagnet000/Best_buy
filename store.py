import products


class Store:
    # get a list of products
    def __init__(self, list_of_products):
        self.list_of_products = list_of_products

    # adds a product
    def add_product(self, product):
        self.list_of_products.append(product)

    # gets rid of a product
    def remove_product(self, product):
        self.list_of_products.remove(product)

    # looks at all the products parameters and returns total quantity of all individual products
    def get_total_quantity(self):

        total = 0
        for item in self.list_of_products:
            total += item.get_quantity()

        return total

    # looks at all currently active products and returns the list of each
    def get_all_products(self):

        active_products = []

        for item in self.list_of_products:
            item.get_quantity()
            if item.is_active():
                active_products.append(item)

        return active_products

    def order(self, shopping_list):

        total = 0

        for item in shopping_list:
            total += item[0].buy(item[1])

        return total


product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250),
                ]


