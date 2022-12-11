#!/usr/bin/env python3

import random
import difflib
import math


class WordLogic(object):

    def __init__(self, num_words, len_words):
        self.num_words = num_words
        self.len_words = len_words

    def is_similar(self, a, b, threshold):
        s = difflib.SequenceMatcher(None, a, b)
        return True if s.ratio() > threshold else False

    def find_words_with_right_size(self):
        with open("resource/words.txt") as f:
            word_list = f.read().splitlines()
        return [word.upper() for word in word_list if len(word) is self.len_words]

    def word_selection(self):
        words = self.find_words_with_right_size()
        random.shuffle(words)
        selected_words = words[:math.floor(self.num_words / 3)]  # choose one third of shuffled words
        rest = words[math.floor(self.num_words / 3):]            # rest of shuffled words

        while len(selected_words) < self.num_words:
            rand_selected_words = random.choice(selected_words)
            rand_rest = random.choice(rest)

            if self.is_similar(rand_selected_words, rand_rest, 0.4):
                selected_words.append(rand_rest)
                rest.remove(rand_rest)

        return selected_words
