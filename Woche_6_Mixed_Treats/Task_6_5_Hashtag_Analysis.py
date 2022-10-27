
def analyze(posts):

    all_hashtags = []
    hash_dict = {}

    for line in posts:
        hashtag = ""
        pos_hashtags = line.split("#")      # all possible hashtags, but invalid Characters are included
        pos_hashtags.pop(0)                 # first one is always False

        for word in pos_hashtags:
            for i in range(len(word)):
                if i + 1 == len(word) and word[i].isalnum():    # when full word is a Hashtag
                    hashtag = word
                if not word[i].isalnum():                       # end of Hashtag
                    hashtag = word[:i]
                    break
            if hashtag:
                if hashtag[0].isalpha():
                    all_hashtags.append(hashtag)

    for hashtag in all_hashtags:
        hash_dict[hashtag] = all_hashtags.count(hashtag)

    return hash_dict


posts = [
    "hi #weekend",
    "good morning #zurich #limmat",
    "spend my #weekend in #zurich",
    "#zurich <3 # #1wer"
]
print(analyze(posts))
