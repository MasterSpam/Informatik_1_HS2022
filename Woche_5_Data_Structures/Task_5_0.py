l = [2, 7, 5, 'two', 'seven', 11]
for el in l:
    print(el)

for index in range(len(l)):
    print(f"l[{index}] = {l[index]}")

for index, val in enumerate(l):
    print(f"l[{index}] = {val}")
