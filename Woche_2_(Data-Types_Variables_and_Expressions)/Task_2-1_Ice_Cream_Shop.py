price_cone = 0.70
price_per_scoop_vanilla = 1.00
price_per_scoop_chocolate = 1.10

num_scoops_vanilla = 1
num_scoops_chocolate = 3


def get_price():

    price = price_cone + (num_scoops_chocolate * price_per_scoop_chocolate) + (num_scoops_vanilla * price_per_scoop_vanilla)

    return price


print(get_price())
print()
