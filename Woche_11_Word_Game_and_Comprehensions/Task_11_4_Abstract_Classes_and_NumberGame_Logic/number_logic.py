#!/usr/bin/env python3

from game_logic import GameLogic
import random

class NumberLogic(GameLogic):

    def __init__(self, num_words, len_words, num_attempts):
        super().__init__(num_words, len_words, num_attempts)
        self.num_words = num_words
        self.len_words = len_words
        self.num_attempts = num_attempts
        num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(num_words):
            pass


