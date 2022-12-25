# create a function that creates an index of words from a given list of strings (dataset)
# the index should be a dictionary where the keys are the words and the values are lists of indices of the strings in the dataset where the word appears
# the words should be case insensitive
# the words should be stored in the dictionary as lowercase
# the indices should be stored in ascending order
# the function should return the index as a dictionary
#
# example:
# dataset = ['The sun is shining', 'The weather is sweet', 'The sun is shining, the weather is sweet, and one and one is two']
# print(reverse_index(dataset)) # prints {'and': [2], 'is': [0, 1, 2], 'one': [2], 'shining': [0, 2], 'sun': [0, 2], 'sweet': [1, 2], 'the': [0, 1, 2], 'two': [2], 'weather': [1]}

def reverse_index(dataset):

    index_dictionary = {}

    # Loop through dataset
    for index,current_data in enumerate(dataset) :
        # Split current_data to find words
        word_list = current_data.split()
        # Loop through wordList
        for current_word in word_list:
            # Make the word case insensitive by converting it to lowercase
            current_word = current_word.lower()
            # Append the index of the word to the dictionary
            if current_word not in index_dictionary:
                index_dictionary[current_word] = [] # create a list with the key if it doesn't exist
            index_dictionary[current_word].append(index) # append the key to the list

    return index_dictionary

dataset = [
    "Hello world",
    "This is the WORLD",
    "hello again"
 ]
print(reverse_index(dataset))
# prints {'hello': [0, 2], 'world': [0, 1], 'this': [1], 'is': [1], 'the': [1], 'again': [2]}