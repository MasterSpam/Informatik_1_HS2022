
# build a string
def build_string_pyramid(h):
    # init for h = 0
    s = ""

    # build the first half of the pyramid
    for i in range(1, h + 1):
        for j in range(1, i + 1):
            s += str(j)
            if j < i:
                s += "*"
        s += "\n"

    # build the second half of the pyramid
    for i in range(h - 1, 0, -1):
        for j in range(1, i + 1):
            s += str(j)
            if j < i:
                s += "*"
        s += "\n"

    return s

h = 10 # height of the pyramid (number of rows)
print(build_string_pyramid(h))
# prints the following:
# 1
# 1*2
# 1*2*3
# 1*2*3*4
# 1*2*3*4*5
# 1*2*3*4*5*6
# 1*2*3*4*5*6*7
# 1*2*3*4*5*6*7*8
# 1*2*3*4*5*6*7*8*9
# 1*2*3*4*5*6*7*8*9*10
# 1*2*3*4*5*6*7*8*9
# 1*2*3*4*5*6*7*8
# 1*2*3*4*5*6*7
# 1*2*3*4*5*6
# 1*2*3*4*5
# 1*2*3*4
# 1*2*3
# 1*2
# 1
