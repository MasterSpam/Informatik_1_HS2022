# create a function that analyzes a list of posts and returns a dictionary with the hashtags as keys and the number of times they appear as values
# the function should return an empty dictionary if the list of posts is empty
# the function should return an empty dictionary if there are no hashtags in the list of posts

def analyze(posts):
    tags = {}

    for post in posts:
        curHashtag = None
        for c in post:
            is_allowed_char = c.isalnum()

            if curHashtag != None and not is_allowed_char:
                if len(curHashtag) > 0 and not curHashtag[0].isdigit():
                    if curHashtag in tags.keys():
                        tags[curHashtag] += 1
                    else:
                        tags[curHashtag] = 1
                curHashtag = None

            if c == "#":
                curHashtag = ""
                continue

            if c.isalnum() and curHashtag != None:
                curHashtag += c

        if curHashtag != None:
            if len(curHashtag) > 0 and not curHashtag[0].isdigit():
                if curHashtag in tags.keys():
                    tags[curHashtag] += 1
                else:
                    tags[curHashtag] = 1

    return tags

# test cases
posts = [ "This is a post with no hashtags", "This is a post with #one #hashtag", "This is a post with #two #hashtags", "This is a post with #three #hashtags #and #a #few #more" ]
print(analyze(posts)) # {'one': 1, 'hashtag': 1, 'two': 1, 'hashtags': 1, 'three': 1, 'and': 1, 'a': 1, 'few': 1, 'more': 1}
