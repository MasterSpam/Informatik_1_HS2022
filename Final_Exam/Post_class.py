from abc import ABC, abstractmethod


class Postcard(ABC):

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price


class Wrapper:

    def __init__(self, contents):
        self.contents = contents

    @abstractmethod
    def get_number_of_postcards(self):
        pass

    @abstractmethod
    def get_price(self):
        pass

    def get_contents(self):
        return self.contents


class Envelope(Wrapper):
    def __init__(self, contents):
        if len(contents) < 2 or len(contents) > 7:
            raise Warning()
        super().__init__(contents)

    def get_number_of_postcards(self):
        return len(self.contents)

    def get_price(self):
        return round(sum([content.get_price() for content in self.contents]), 2)


class Package(Wrapper):
    package_id = 1

    def __init__(self, contents):

        if sum([envelopes.get_number_of_postcards() for envelopes in contents]) > 150:
            raise Warning()

        super().__init__(contents)

        self.id = Package.package_id
        Package.package_id += 1

    def get_number_of_postcards(self):
        return sum([envelopes.get_number_of_postcards() for envelopes in self.contents])

    def get_price(self):
        return round(sum([envelopes.get_price() for envelopes in self.contents]), 2)

    def get_id(self):
        return self.id


def make_postcards(n):
    return [Postcard("Christmas", 0.25) if x % 2 == 0 else Postcard("Beach", 0.70) for x in range(n)]


postcards = make_postcards(4)
print(postcards[0].get_name())
print(postcards[0].get_price())

w1 = Envelope(postcards)
print([c.get_name() for c in w1.get_contents()])

w2 = Envelope(make_postcards(4))
b = Package([w1, w2])
print(f"\nPostcards in package: {b.get_number_of_postcards()}")
print(f"  Price of package: {b.get_price()}")
print(f"     ID of package: {b.get_id()}\n")

more_envelopes = [Envelope(make_postcards(4)) for x in range(52)]  # 208 postcards
try:
    overfull = Package(more_envelopes)
except Warning:
    print("Too many postcards for one package\n")
