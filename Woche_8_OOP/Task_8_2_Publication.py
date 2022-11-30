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
        return self.__str__()

    def __eq__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        return self.__is_equal(other)

    def __ne__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        return not self.__is_equal(other)

    def __lt__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        return self.__is_less(other)

    def __le__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        return self.__is_less(other) or self.__is_equal(other)

    def __gt__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        return not (self.__is_less(other) or self.__is_equal(other))

    def __ge__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        return not self.__is_less(other)

    def __is_equal(self, other) -> bool:
        return self.get_unique_hash() == other.get_unique_hash()

    def __is_less(self, other) -> bool:
        if self.get_authors() == other.get_authors():
            if self.get_title() == other.get_title():
                return self.get_year() < other.get_year()
            else:
                return self.get_title() < other.get_title()
        else:
            return self.get_authors() < other.get_authors()

    def __hash__(self):
        return self.get_unique_hash()

    def get_unique_hash(self) -> int:
        return hash(tuple(self.__authors) + (self.__title, str(self.__year)))

    def get_authors(self):
        copy = []
        for i in self.__authors:
            copy.append(i)
        return copy

    def get_title(self):
        return self.__title

    def get_year(self):
        return self.__year


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
