import random
from unittest import TestCase
from Task_12_1_script_Make_it_Simple import find_in, find_in_refactored


class TaskTestSuite(TestCase):

    def test_find_in_empty_list(self):
        test_pairs = []
        self.assertEqual(None, find_in(test_pairs))
        self.assertEqual(None, find_in_refactored(test_pairs))

    def test_find_in_one_pair(self):
        test_pairs = [('A', 1)]
        self.assertEqual('A', find_in(test_pairs))
        self.assertEqual('A', find_in_refactored(test_pairs))

    def test_find_in_many_pairs(self):
        test_pairs = [('A', 1), ('B', 2), ('C', 3), ('D', 4)]
        self.assertEqual('A', find_in(test_pairs))
        self.assertEqual('A', find_in_refactored(test_pairs))

    def test_find_in_many_pairs_with_repetition(self):
        test_pairs = [('A', 1), ('B', 2), ('C', 3), ('D', 4), ('A', 1), ('B', 2)]
        self.assertEqual('A', find_in(test_pairs))
        self.assertEqual('A', find_in_refactored(test_pairs))

    def test_find_in_many_pairs_with_random_order(self):
        test_pairs = [('A', 1), ('B', 2), ('C', 3), ('D', 4)]
        random.shuffle(test_pairs)
        self.assertEqual('A', find_in(test_pairs))
        self.assertEqual('A', find_in_refactored(test_pairs))
