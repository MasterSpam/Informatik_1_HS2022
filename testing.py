import string

# List of letter frequencies in English
letter_goodness = [.0817, .0149, .0278, .0425, .1270, .0223, .0202,
                   .0609, .0697, .0015, .0077, .0402, .0241, .0675,
                   .0751, .0193, .0009, .0599, .0633, .0906, .0276,
                   .0098, .0236, .0015, .0197, .0007]

# List of uppercase letters in the alphabet
alphabet = list(string.ascii_uppercase)

# Get encoded string from user
encoded_string = input("Your encoded string: ").upper()

# Initialize variables
best_decoded_string = ""
highest_goodness = 0

# Try all possible shifts
for shift in range(26):
    decoded_string = ""
    goodness = 0

    # Decode each character in the encoded string
    for char in encoded_string:
        index = alphabet.index(char)
        decoded_char = alphabet[(index + shift) % 26]
        decoded_string += decoded_char
        goodness += letter_goodness[index]

    # Update best decoded string and highest goodness if necessary
    if goodness > highest_goodness:
        highest_goodness = goodness
        best_decoded_string = decoded_string

# Print the best decoded string
print(best_decoded_string)
