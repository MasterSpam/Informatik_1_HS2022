#!/usr/bin/env python3

from random import choice, shuffle
from game_logic import GameLogic


# This is the current version of WordLogic that needs to be adapted
class WordLogic(GameLogic):

    def __init__(self, num_words, len_words, num_attempts):
        super().__init__(num_words, len_words, num_attempts)
        self.num_words = num_words
        self.len_words = len_words
        self.num_attempts = num_attempts
        self.words = self._word_selection()
        self.password = choice(self.words)

    def _word_selection(self):
        words = self._find_words_with_right_size()
        shuffle(words)
        return words[0:self.num_words]

    def _find_words_with_right_size(self):
        with open("resource/words.txt") as f:
            word_list = f.read().splitlines()
        return [word.upper() for word in word_list if len(word) is self.len_words]

    def check(self, guess):
        if self.num_attempts == 0:
            raise Warning("No attempts left")
        if len(guess) != self.len_words:
            return False, ["Wrong length"]
        if guess == self.password:
            return True, ["Access granted!"]
        else:
            return False, [
                self._generate_feedback(guess),
                "Access denied!"
            ]

    def _generate_feedback(self, guess):
        matching = 0
        for i in range(self.len_words):
            if guess[i] == self.password[i]: matching += 1
        self.num_attempts = self.num_attempts - 1
        return "%d/%d correct" % (matching, self.len_words)
