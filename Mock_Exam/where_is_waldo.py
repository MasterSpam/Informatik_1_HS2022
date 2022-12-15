
def where_is_waldo(names):
    if "Waldo" in names:
        return names.index("Waldo")


print(where_is_waldo(["Peter", "Waldo", "John"]))
print(where_is_waldo(["Peter", "Willy", "John"]))