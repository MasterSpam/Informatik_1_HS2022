import json


class Publication:

    def __init__(self, authors, title, year):
        self.__authors = authors
        self.__authors = json.dumps(self.__authors)
        self.__title = '"' + title + '"'
        self.__year = year

    def __str__(self):
        return f"{__class__.__name__}({self.__authors}, {self.__title}, {self.__year})"

    def __repr__(self):
        return self.__str__(self)

    def __eq__(self, other):
        return self.__str__() == other.__str__()

    def __hash__(self):
        return self.__year

    def __lt__(self, other):    # x < y
        if not isinstance(other, self):
            return NotImplemented
    # check is self.__authors < other.__authors or self.__title < other.__title or self.__year < other.year: True

    object.__lt__(self, other)
    object.__le__(self, other)
    object.__eq__(self, other)
    object.__ne__(self, other)
    object.__gt__(self, other)
    object.__ge__(self, other)


# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    references = [
        Publication(["Gamma", "Helm", "Johnson", "Vlissides"], "Design Patterns", 1994),
        Publication(["Cockburn"], "Writing Effective Use Cases", 2000),
        Publication(["Duvall", "Matyas", "Glover"], "Continuous Integration", 2007)
    ]

    p = Publication(["Duvall", "Matyas", "Glover"], "Continuous Integration", 2007)
    s = "Publication([\"Duvall\", \"Matyas\", \"Glover\"], \"Continuous Integration\", 2007)"
    print(p)
    print(str(p) == s)

    p1 = Publication(["A"], "B", 1234)
    p2 = Publication(["A"], "B", 1234)
    p3 = Publication(["B"], "C", 2345)
    print(p1 == p2)  # True
    print(p2 == p3)  # False

    sales = {
        p1: 273,
        p2: 398,
    }
