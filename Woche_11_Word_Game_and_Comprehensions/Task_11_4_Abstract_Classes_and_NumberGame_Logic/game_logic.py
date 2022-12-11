#!/usr/bin/env python3

from abc import ABC, abstractmethod


class GameLogic(ABC):

    def __init__(self, num_words, len_words, num_attempts):
        self.num_words = num_words
        self.len_words = len_words
        self.num_attempts = num_attempts

    @abstractmethod
    def check(self, guess):
        pass

    @abstractmethod
    def _word_selection(self):
        pass

    @abstractmethod
    def _generate_feedback(self):
        pass
