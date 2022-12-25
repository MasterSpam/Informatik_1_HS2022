

class Event:

    def __init__(self, seats):
        self._seats = seats
        self._stadium = {}

    def enter(self, seat_number, name):
        if 1 > seat_number > self._seats:
            raise IndexError
        if seat_number in self._stadium:
            raise NameError
        self._stadium[seat_number] = name

    def get(self, seat_number):
        if 1 > seat_number > self._seats:
            raise IndexError
        if seat_number in self._stadium:
            return self._stadium[seat_number]

    def occupied(self):
        occupied = 0
        for seat in self._stadium:
            if seat in self._stadium:
                occupied += 1
        return occupied

    def empty(self):
        return self._seats - self.occupied()

    def __lt__(self, other):
        return self.occupied() < other.occupied()

    def __gt__(self, other):
        return self.occupied() > other.occupied()

    def __eq__(self, other):
        return self.occupied() == other.occupied()


# DO NOT SUBMIT THE LINES BELOW!
e1 = Event(150)
e1.enter(45, "Alice")
assert e1.get(45) == "Alice"
e1.enter(42, "Bob")
assert e1.occupied() == 2
assert e1.empty() == 148
e2 = Event(40)
assert e2.get(40) == None
e2.enter(1, "Andrea")
e2.enter(2, "Beatrice")
assert e2 == e1
e2.enter(20, "Charly")
assert e2 > e1
