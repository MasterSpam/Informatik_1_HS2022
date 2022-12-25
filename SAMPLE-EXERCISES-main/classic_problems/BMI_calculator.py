#Write a program that determines the right BMI catergory for a given height and weight. The height in metres and weight in kg are provided in a float variables called height and weight, respectively. The BMI category is calculated by a function called get_bmi_category and your task is to complete the function.

#Please make sure that your solution is self-contained within the get_bmi_category function. That is, only change the body of the function, not the code outside the function. Your function is expected to return the right category in a string and the BMI to 2 decimal places. For example, if the height is 1.75 and the weight is 80, the function should return the string "BMI: 26.12, Category: Pre-obesity". If the user enters a negative height or weight, the function should return the string "N/A".

def get_bmi_category(height, weight):
    # your code goes here
    if height < 0 or weight < 0:
        return "N/A"
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        return "BMI: {:.2f}, Category: Underweight".format(bmi)
    elif bmi < 25:
        return "BMI: {:.2f}, Category: Normal".format(bmi)
    elif bmi < 30:
        return "BMI: {:.2f}, Category: Pre-obesity".format(bmi)
    elif bmi < 35:
        return "BMI: {:.2f}, Category: Obesity class I".format(bmi)
    elif bmi < 40:
        return "BMI: {:.2f}, Category: Obesity class II".format(bmi)
    else:
        return "BMI: {:.2f}, Category: Obesity class III".format(bmi)

# DO NOT CHANGE THE CODE BELOW
height = float(input("Enter height in metres: "))
weight = float(input("Enter weight in kg: "))
print(get_bmi_category(height, weight))

# Sample run
# Enter height in metres: 1.75
# Enter weight in kg: 80
# BMI: 26.12, Category: Pre-obesity

