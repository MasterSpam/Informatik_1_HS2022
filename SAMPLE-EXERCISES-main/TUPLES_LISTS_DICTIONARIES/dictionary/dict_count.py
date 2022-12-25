# create a function that counts the number of occurrences of each word in a given string
# the function should return a dictionary with the words as keys and the number of occurrences as values
# the words should be case insensitive
# the words should be stored in the dictionary as lowercase
# the function should return an empty dictionary if the input string is empty
#


def count_words(s):
    word_count = {}
    if s == "":
        return word_count
    else:
        word_list = s.split()
        for word in word_list:
            word = word.lower()
            if word not in word_count:
                word_count[word] = 1
            else:
                word_count[word] += 1
        return word_count

s = "The sun is shining, the weather is sweet, and one and one is two"
print(count_words(s))
# prints {'and': 2, 'is': 3, 'one': 2, 'shining,': 1, 'sun': 1, 'sweet,': 1, 'the': 2, 'two': 1, 'weather': 1}

