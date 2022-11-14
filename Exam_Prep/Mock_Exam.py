# Calling hello('Jim') should return "Hello, Jim!"
def hello(name):
    return f"Hello, {name}"


# where_is_waldo(["Peter", "Waldo", "John"]) should return 1
# where_is_waldo(["Peter", "Willy", "John"]) should return -1
def where_is_waldo(names):
    if "Waldo" not in names:
        return -1
    return names.index("Waldo")
