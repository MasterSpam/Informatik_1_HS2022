#!/usr/bin/env python3

# The signatures of this class and its public methods are required for the automated grading to work.
# You must not change the names or the list of parameters.
# You may introduce private/protected utility methods though.
class ProfanityFilter:

    def __init__(self, keywords, template):
        self.__swearwords = list(map(lambda s: s.lower(), sorted(keywords, key=len, reverse=True)))
        self.__censor = template

    @staticmethod
    def __clean(bad_word, my_censor):
        long_censor = my_censor * (len(bad_word) // len(my_censor) + 1)
        return long_censor[:len(bad_word)]

    def filter(self, msg):
        temp_text = msg.lower()

        for word in self.__swearwords:
            indices = [i for i in range(len(temp_text)) if temp_text.startswith(word, i)]
            cleaned_word = ProfanityFilter.__clean(word, self.__censor)
            for index in indices:
                msg = msg[:index] + cleaned_word + msg[index + len(cleaned_word):]
        return msg


# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
    offensive_msg = "abc defghi mastard jklmno batch"
    clean_msg = f.filter(offensive_msg)
    print(clean_msg)  # abc defghi ?#$?#$? jklmno
