
# If the user enters a negative height or weight, the function should return the string "N/A".
# For invalid categories (i.e., measures outside the limits stated in the table), return "N/A" as the category.
# [0, 18.5]	Underweight
# (18.5, 25] Normal weight
# (25, 30]	Pre-obesity
# (30, 35]	Obesity class I
# (35, 40]	Obesity class II
# (40, ♾️)	Obesity class III

# Height in M
height = 1.8
# Weight in KG
weight = 130


def get_bmi_category():

    bmi = weight/(height**2)
    print(bmi)
    if height < 0 or weight < 0:
        return "N/A"

    if 0 <= bmi <= 18.5:
        category = "Underweight"
    elif 18.5 < bmi <= 25:
        category = "Normal weight"
    elif 25 < bmi <= 30:
        category = "Pre-obesity"
    elif 30 < bmi <= 35:
        category = "Obesity class I"
    elif 35 < bmi <= 40:
        category = "Obesity class II"
    elif bmi > 40:
        category = "Obesity class III"
    else:
        category = "N/A"

    result = f"BMI: {bmi:.2f}, Category: {category}"

    return result


print(get_bmi_category())
