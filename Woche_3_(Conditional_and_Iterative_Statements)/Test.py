
plain_text = "abzAZ!"
shift = -1


def rot_n():

    shift_by = shift % 26
    todo = ""
    for i in plain_text:
        curr = ord(i)
        if i.isalpha ():
            if curr < 91 and curr > 64:
                desiredVal = shift_by + curr
                if(desiredVal> 90):
                    change = desiredVal - 90
                    val = 64 + change
                    s = chr (val)
                    todo += s
                else:
                    todo += chr(desiredVal)
            else:
                desiredVal = shift_by + curr
                if(desiredVal > 122):
                    change = desiredVal - 122
                    val = 96 + change
                    s = chr(val)
                    todo += s
                else:
                    todo += chr (desiredVal)
        else:
            todo += i

    return todo


print(rot_n())
