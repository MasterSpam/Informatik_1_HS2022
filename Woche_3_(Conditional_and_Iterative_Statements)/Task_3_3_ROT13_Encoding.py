
plain_text = "Hallo"
shift_by = 1
a_lower = 97
a_upper = 65

#   a = 97, A = 65


def rot_n():

    encoded = ""

    for char in plain_text:
        if char.isalpha():
            diff = a_lower if char.islower() else a_upper
            encoded += chr((ord(char) - diff + shift_by) % 26 + diff)
        else:
            encoded += char
    return encoded


print(rot_n())
