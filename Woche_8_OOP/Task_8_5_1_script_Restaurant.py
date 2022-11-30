from Task_8_5_3_item_Restaurant import Item
from Task_8_5_2_order_Restaurant import Order


class Restaurant:

    def __init__(self, restaurant_name, menu_list):
        self.__restaurant_name = restaurant_name
        self.__menu_list = menu_list
        self.__order = []

    def get_restaurant_name(self):
        return self.__restaurant_name

    def get_menu_list(self):
        return self.__menu_list

    def get_order_list(self):
        if self.__order:
            return self.__order
        return "No order yet"

    def set_order(self, item_list):
        corrected_item_list = []
        for item in item_list:
            if item  in self.__menu_list:
                corrected_item_list.append(item)
        if len(corrected_item_list) > 0:
            self.__order.append(Order(corrected_item_list))

        new_order = Order(corrected_item_list)

    def get_revenue(self):
        revenue = 0

        for order in self.__order:
            revenue += order.get_bill_amount()

        return revenue


# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    # Create Item Objects with Name and Price
    steak = Item("Steak", 25)
    salad = Item("Salad", 10)
    fish = Item("Fish", 30)
    pizza = Item("Pizza", 40)
    # Create menu list
    menu_list = [steak, salad, fish]
    # Create order list
    order_list = [steak, steak, salad, pizza]
    # Create restaurant object with name and menu list
    restaurant = Restaurant("Zurich_1", menu_list)
    # Create an order with the order list
    restaurant.set_order(order_list)
    # Get the revenue of the restaurant object
    print(restaurant.get_revenue())

    print(restaurant.get_restaurant_name())
