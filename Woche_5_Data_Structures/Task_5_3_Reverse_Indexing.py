# result should be:
# 'hello': [0, 2],
# 'world': [0, 1],
# 'this': [1],
# 'is': [1],
# 'the': [1],
# 'again':[2]

from collections import defaultdict

dataset = [
    "Hello world",
    "This is the WORLD",
    "hello again"
]


def reverse_index(dataset):
    index_dictionary = {}

    for index, string in enumerate(dataset):
        string = string.lower()
        all_words = string.split(" ")
        for word in all_words:
            if word.lower() not in index_dictionary:
                index_dictionary[word] = []
            index_dictionary[word.lower()].append(index)

    return index_dictionary


print(reverse_index(dataset))
