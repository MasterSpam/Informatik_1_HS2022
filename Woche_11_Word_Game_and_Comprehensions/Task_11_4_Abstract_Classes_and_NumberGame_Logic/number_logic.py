#!/usr/bin/env python3

from game_logic import GameLogic
from random import sample


class NumberLogic(GameLogic):

    def _word_selection(self):
        sequences = []

        while len(sequences) < self.num_words:
            sequence = "".join(sample("0123456789", self.len_words))

            if sequence not in sequences:
                sequences.append(sequence)

        return sequences

    def _generate_feedback(self, guess):
        feedback_guess = set(guess)
        feedback_password = set(self.password)

        num_correct = len(feedback_guess.intersection(feedback_password))
        return "%d/%d correct" % (num_correct, self.len_words)

    def check(self, guess):
        if len(guess) != self.len_words:
            raise Warning("Invalid input length!")
        for number in guess:
            if guess.count(number) != 1:
                raise Warning("Input can't have a number more than once!")
        return super().check(guess)
