import products
import store

product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250)
               ]

best_buy = store.Store(product_list)

def restart():
    start(best_buy)

def start(Store_parameter):

    while True:

        print("Store Menu")

        print("----------")

        print("1. List all products in store")
        print('2. Show total amount in store')
        print('3. Make an order')
        print('4. Quit')

        try:
            user_input = int(input("Please chose a number : "))
            if user_input > 4:
                print("Please input a number between 1-4")
                continue
        except (TypeError, ValueError) as e:
            print(f"there seems to be a problem : {e}")
            continue


        if user_input == 1:

            products = best_buy.get_all_products()
            for items in products:
                print(items.show())

            restart()

        elif user_input == 2:
            print(best_buy.get_total_quantity)

        elif user_input == 3:


            best_buy.order(user_choice)


start(best_buy)

