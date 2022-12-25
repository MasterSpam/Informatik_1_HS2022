# -- THIS LINE SHOULD BE THE FIRST LINE OF YOUR SUBMISSION! --#

from abc import ABC, abstractmethod
import unittest


class Product(ABC):

    @abstractmethod
    def get_price(self):
        pass


class Bottle(Product):

    def __init__(self, price, name):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price


class Crate(Product):

    def __init__(self):
        self.__all_bottles = []
        self.__total_price = 0

    def get_price(self):
        return self.__total_price

    def add(self, bottle):
        if len(self.__all_bottles) == 20:
            raise RuntimeError
        self.__all_bottles.append(bottle)
        self.__total_price += bottle.get_price()

    def get_size(self):
        return len(self.__all_bottles)


class DiscountCrate(Crate):
    def __init__(self):
        super().__init__()

    def add(self, bottle):
        super().add(bottle)

    def get_size(self):
        return super().get_size()

    def get_price(self):
        reduction = 1 - self.get_size() * 0.02 if 1 - self.get_size() * 0.02 > 0.75 else 0.75
        return round(super().get_price() * reduction, 2)


class FixedPriceCrate(Crate):
    def __init__(self, price):
        super().__init__()
        self.__price = price

    def add(self, bottle):
        super().add(bottle)

    def get_size(self):
        return super().get_size()

    def get_price(self):
        return self.__price


class ShopTestSuite(unittest.TestCase):

    def test_crate_add(self):
        c = Crate()
        c.add(Bottle(4.50, "Light Beer"))
        self.assertEqual(c.get_size(), 1)

    def test_crate_max_size(self):
        all_bottles = [Bottle(3.50, "Light Beer")] * 20
        c = Crate()
        for b in all_bottles: c.add(b)
        with self.assertRaises(RuntimeError):
            c.add(Bottle(3.50, "Light Beer"))

    def test_crate_price(self):
        test_bottles = [Bottle(3.50, "Light Beer"), Bottle(4.50, "Passable Wine")] + 3 * [Bottle(4.00, "Strong Stuff")]
        c = Crate()
        for b in test_bottles: c.add(b)
        self.assertEqual(20.00, c.get_price())

    def test_discount_crate_price(self):
        test_bottles = [Bottle(3.50, "Light Beer"), Bottle(4.50, "Passable Wine")] + 3 * [Bottle(4.00, "Strong Stuff")]
        c = DiscountCrate()
        for b in test_bottles: c.add(b)
        self.assertEqual(18.00, c.get_price())


# -- THIS LINE SHOULD BE THE LAST LINE OF YOUR SUBMISSION! ---#

# DO NOT SUBMIT THE FOLLOWING LINES!!! THESE ARE FOR LOCAL TESTING ONLY!
bottles = [Bottle(3.50, "Light Beer"), Bottle(4.50, "Passable Wine")] + 3 * [Bottle(4.00, "Strong Stuff")]
assert (bottles[0].get_price() == 3.50)

c = Crate()
for b in bottles: c.add(b)
assert (c.get_size() == 5)
assert (c.get_price() == 20.00)

c = FixedPriceCrate(11.11)
for b in bottles: c.add(b)
assert (c.get_price() == 11.11)

c = DiscountCrate()
for b in bottles: c.add(b)
assert (c.get_price() == 18.00)

unittest.main()
