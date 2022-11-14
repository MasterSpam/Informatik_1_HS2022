# For each executive room, one parking space is offered for free
# For each suite room, one parking space and one breakfast are offered for free
# If at least 3 rooms of any type are booked, all room prices are reduced by 10%

milton_hotel = {
    "standard": 120.00,
    "executive": 160.00,
    "suite": 320.00,
    "breakfast": 25.00,
    "parking": 30.00,
}


def booking(pricing, products):
    brutto_sum = 0
    netto_sum = 0
    factor = 1

    # calculate everything
    for element in products:
        brutto_sum += pricing[element]

    # calculate with discount
    temp_product = products
    if products.count("standard") + products.count("executive") + products.count("standard") >= 3:
        factor = 0.9
    for element in products:

        if element == "executive":
            netto_sum += pricing[element] * factor

        elif element == "suite":
            netto_sum += pricing[element] * factor

        elif element == "standard":
            netto_sum += pricing[element] * factor
        else:

            netto_sum += pricing[element]
        if element == "executive":
            if "parking" in temp_product:
                temp_product.remove("parking")
                netto_sum -= pricing["parking"]

        if element == "suite":
            if "parking" in temp_product:
                temp_product.remove("parking")
                netto_sum -= pricing["parking"]
            if "breakfast" in temp_product:
                temp_product.remove("breakfast")
                netto_sum -= pricing["breakfast"]

    return brutto_sum, brutto_sum - netto_sum, netto_sum


print(booking(milton_hotel, [  # no discounts
    "executive", "breakfast"
]))
print(booking(milton_hotel, [  # one free parking
    "standard", "executive", "breakfast", "breakfast", "parking"
]))
print(booking(milton_hotel, [  # two free parking (one applied) and one free breakfast plus 10% off all rooms
    "standard", "executive", "suite", "parking",
    "breakfast", "breakfast", "breakfast"
]))
