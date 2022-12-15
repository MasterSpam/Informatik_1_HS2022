
###################################
# RECURSION
###################################
def rec_sum(l):
    if not l:
        return 0
    return l[0] + rec_sum(l[1:])


rec_list = [1, 2 ,3]
print(f"recursive sum of {rec_list} is : {rec_sum([1,2,3])}\n")


def add_something(n, l):
    if not l:
        return []
    elem = l[0] + n
    return [elem] + add_something(n, l[1:])


adding = 3
add_list = [2, 3 ,4]
print(f"if you add {adding} to the list {add_list} the result is: {add_something(adding, rec_list)}\n")

###################################
# CLASSES
###################################


class File:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class Folder(File):
    def __init__(self, name):
        super().__init__(name)
        self.files = []

    def add_file(self, f):
        self.files.append(f)

    def __repr__(self):
        return self.name + ": " + str(self.files)


f = File("vacation.jpg")
root = Folder("vacation pics")

bahamas = Folder("bahamas")
bahamas.add_file(f)

root.add_file(bahamas)
print(root)

