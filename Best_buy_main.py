import products
import store
import promotions


# setup initial stock of inventory
product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250),
                 products.NonStockedProduct("Windows License", price=125),
                 products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
               ]

# Create promotion catalog
second_half_price = promotions.SecondHalfPrice("Second Half price!")
third_one_free = promotions.ThirdOneFree("Third One Free!")
thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

# Add promotions to products
product_list[0].set_promotion(second_half_price)
product_list[1].set_promotion(third_one_free)
product_list[3].set_promotion(thirty_percent)

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

        # lists all products
        if user_input == 1:

            products = best_buy.get_all_products()
            for items in products:
                print(items.show())
            restart()

        # shows the total product quantity in the store
        elif user_input == 2:
            print(f" Total of {best_buy.get_total_quantity()} items in store")

        # creates an order and total for items and quantity chosen
        elif user_input == 3:

            # creates a variable with a list of products.
            choices = best_buy.get_all_products()
            customer_order = []
            check_max = {}

            total = 0

            # prints numerical items
            for choice in range(len(choices)):
                print(f"{choice + 1}. {choices[choice].show()}")

            while True:
                # uses try to catch any unexpected inputs and errors
                try:

                    # corrects user choice to correct list item
                    user_choice = int(input("Which product number do you want? : ")) - 1

                    # makes sure the choice is not out of list index
                    if user_choice > len(choices):
                        print("Error choice not found")
                        continue

                    # gets the quantity desired
                    amount_choice = float(input("What amount would you like? : "))

                    #checks if choice/s is used more than maximum amount or ordered over maximum amount
                    if choices[user_choice].LimitedProduct:
                        if choices[user_choice].name in check_max:
                            accumilated_amount = check_max[choices[user_choice].name]
                        else:
                            accumilated_amount = 0
                        if amount_choice + accumilated_amount > choices[user_choice].maximum:
                            print(f"This order has excided the maximum amount {choices[user_choice].maximum}")
                            ask_if_user_wants_more_items = input("Would you like more items? Y/N :").upper()
                            if ask_if_user_wants_more_items == "Y":
                                continue
                            break
                        if choices[user_choice].name not in check_max:
                            check_max[choices[user_choice].name] = amount_choice
                        else:
                            if check_max[choices[user_choice].name] >= choices[user_choice].maximum:
                                print(f"too much")
                                continue
                            check_max[choices[user_choice].name] += amount_choice

                    # gathers the information needed into a single list item
                    customer_order.append([choices[user_choice], amount_choice])


                    # updates the total
                    total += best_buy.order(customer_order)

                    customer_order.remove(customer_order[-1])

                    print(f"Your current total is : {total}")

                    # offers the customers an option to add more items to their basket
                    ask_if_user_wants_more_items = input("Would you like more items? Y/N :").upper()
                    if ask_if_user_wants_more_items == "Y":
                        continue
                    break
                except (TypeError, ValueError) as e:
                    print(f"There was a problem with you input : {e}")
                    continue
            # returns order total
            print("Order Complete!")
            print(f"Your purchace Total : {total} ")


        # exits the program
        elif user_input == 4:

            print(
                "--------- Program Terminated ---------" "\n" "\n" "         Thank you take care          " "\n" "\n" "--------------------------------------")
            exit()


def main():
    start(best_buy)


if __name__ in "__main__":
    main()