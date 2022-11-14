#!/usr/bin/env python3

# Implement this function
#
# This signature is required for the automated grading to work.
# You must not rename the function or change its list of parameters.
def convert_roman_to_int(roman):
    roman_single_digits = {
        # simple cases
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    roman_double_digits = {
        # compound cases
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900
    }

    num = 0
    digit_2 = ""
    all_summands = []
    error = False
    counter = 0

    if len(roman) == 1:
        if roman in roman_single_digits:
            return roman_single_digits[roman]
        raise Warning("Invalid Input")

    if roman in roman_double_digits:
        return roman_double_digits[roman]

    for digit in roman:

        if digit not in roman_single_digits:
            raise Warning("Invalid Input")

        digit_1 = digit_2
        digit_2 = digit

        if digit_1 + digit_2 in roman_double_digits:        # special digit

            try:
                if digit_1 == roman[counter + 1]:           # wrong order "IVII"
                    error = True
            except:
                pass

            try:
                if digit == roman[counter - 2] and digit != "I":          # wrong order "VIV"
                    error = True
            except:
                pass

            num += roman_double_digits[digit_1 + digit_2]
            if digit_2:
                num -= roman_single_digits[digit_1]

            all_summands.pop()
            all_summands.append(roman_double_digits[digit_1 + digit_2])
            try:
                if all_summands[-1] == all_summands[-2]:  # two following same "special digits"
                    error = True
            except:
                pass

        else:                                           # "normal" digit

            num += roman_single_digits[digit]
            all_summands.append(roman_single_digits[digit])
            try:
                if all_summands[-1] == all_summands[-2] == all_summands[-3] == all_summands[-4] and digit != "M":
                    error = True
            except:
                pass

            try:
                if all_summands[-1] == all_summands[-2] and all_summands[-1] != 1 and digit != "M" and digit != "X"\
                        and digit != "C":
                    error = True
            except:
                pass
        counter += 1

    print(all_summands)
    print(sorted(all_summands, reverse=True))

    if all_summands != sorted(all_summands, reverse=True):
        raise Warning("Invalid Input")

    if error:
        raise Warning("Invalid Input")
    return num

# The following lines calls the function and prints the return
# value to the Console.
# i = convert_roman_to_int("VIV")
# print(i)
