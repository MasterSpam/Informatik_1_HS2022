
class Order:

    def __init__(self, items, cost):
        self.items = items
        self.cost = cost

    def __eq__(self, other):
        if isinstance(other, Order):
            return self.cost == other.cost and self.items == other.items
        else:
            return False

    def __ne__(self, other):
        return not self == other



print( Order(["Beer", "Wine", "Beer"], 14.50) == Order(["Wine", "Beer", "Beer"], 14.50))
print( Order(["Beer", "Wine", "Beer"], 14.50) != Order(["Wine", "Beer"], 14.50))
print( Order(["Beer", "Pretzels"], 14.50) == "Healthy meal" )