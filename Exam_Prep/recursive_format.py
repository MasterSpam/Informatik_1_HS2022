def recursive_format(tree):
    





assert (recursive_format([]) == "")
assert (recursive_format([[]]) == "()")
assert (recursive_format(["Hi", "there", ["Jack", "and", "Bobby"], "!"])
        == "Hi there (Jack and Bobby) !")
assert (recursive_format(["What", "is", ["going", ["on"], "here?"]])
        == "What is (going (on) here?)")
