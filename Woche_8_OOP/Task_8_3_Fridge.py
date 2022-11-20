
class Fridge:

    def __init__(self):
        # create fridge storage
        self.__my_fridge = []

    def store(self, product):
        # store product in my_fridge
        self.__my_fridge.append(product)

    def __iter__(self):
        self.__my_fridge.sort()
        # returns iterable list of products
        return self.__my_fridge.__iter__()

    def __len__(self):
        return len(self.__my_fridge)

    def take(self, rem_product):
        """
        :param rem_product: list with products
        :return: first matching item or raise Warning
        """
        if rem_product not in self.__my_fridge:
            raise Warning
        self.__my_fridge.remove(rem_product)
        return rem_product

    def find(self, find_product):
        # finds the earliest matching product or returns none
        __sorted_by_date = sorted(self.__my_fridge, key=lambda tup: tup[0])
        for element in __sorted_by_date:
            if element[1] == find_product:
                return element
        return None

    def take_before(self, date):
        # removes every element with a date that is before the input date
        __sorted_by_date = sorted(self.__my_fridge, key=lambda tup: tup[0])
        __outdated = []
        for element in __sorted_by_date:
            if element[0] < date:
                self.take(element)
                __outdated.append(element)
        return __outdated


if __name__ == '__main__':
    f = Fridge()
    f.store((191127, "Butter"))
    f.store((191127, "Butter"))
    f.store((191124, "Milk"))
    f.store((191117, "Milk"))
    f.store((191227, "Bread"))
    f.store((191125, "Honey"))

    print("Items in the fridge:")
    for i in f:
        print("- {} ({})".format(i[1], i[0]))

    print("Taken out:")
    print(f.take((191127, "Butter")))   # ok
    # f.take((191207, "Bread"))  # fails

    print("Found in Fridge:")
    print(f.find("Milk"))

    print("Items in the fridge:")
    for i in f:
        print("- {} ({})".format(i[1], i[0]))

    print("Remove cause of date:")
    print(f.take_before(191130))

    print("Items in the fridge:")
    for i in f:
        print("- {} ({})".format(i[1], i[0]))


