#!/usr/bin/env python3

class Fridge:

    def __init__(self):
        self.__contents = []
        self.__item_amt = 0
        self.__iterpos = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.__iterpos > len(self.__contents) - 1:
            self.__iterpos = 0
            raise StopIteration

        iter = self.__contents[self.__iterpos]
        self.__iterpos += 1
        return iter

    def __len__(self):
        return self.__item_amt

    def store(self, tuple):
        self.__contents.append(tuple)
        self.__item_amt += 1
        self.__contents.sort()

    def take(self, tuple):
        for item in self.__contents:
            if item == tuple:
                self.__contents.remove(item)
                self.__item_amt -= 1
                return item
        raise Warning("Desired item is not in the fridge")

    def find(self, tpl):

        for item in self.__contents:
            if item[1] == tpl[1]:
                return item
        return None

    def take_before(self, date):
        waste_list = []
        for item in self.__contents:
            if item[0] < date:
                waste_list.append(item)

        for item in waste_list:
            self.__contents.remove(item)
            self.__item_amt -= 1
        return waste_list

    def get_contents(self):
        return self.__contents


f = Fridge()
f.store((191127, "Butter"))
f.store((221117, "Milk"))
f.store((191117, "Milk"))
f.store((201017, "Milk"))

f.store((330101, "Orange"))
f.store((330101, "Apple"))

print("Items in the fridge:")
for i in f:
    print("- {} ({})".format(i[1], i[0]))

print(len(f))

print(f.find((211117, "Milk")))

print(f.get_contents())
f.take_before(211201)
print(f.get_contents())
