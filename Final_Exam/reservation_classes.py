
class Train:

    def __int__(self, name, destination):
        self.name = name
        self.destination = destination
        self.train = []

    def board(self, train_riders):
        pass

    def parse_reservations(self, all_reservations):
        all_people = all_reservations.split(';')


riders = Train.parse_reservations(("Montgomery,Rich,GA;Tim,Merchant,GA;Sally,Sale,D;Peter,Poor,M"))
a = Train("IC17", "Columbus")
a.board(riders)
print(a.get_riders())
p = a.get_riders("GA")
print(type(p[1]))
print(p[1])