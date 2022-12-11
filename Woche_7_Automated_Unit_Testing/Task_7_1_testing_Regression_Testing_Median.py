#!/usr/bin/env python3
from unittest import TestCase
from Task_7_1_script_Regression_Testing_Median import median


# Extend the test suite with regression tests that cover the
# meaningful bug reports. Make sure that you define test methods
# and that each method _directly_ includes an assertion in the
# body, or -otherwise- the grading will mark the test suite as
# invalid.

# User 1: Super annoying! I collect all my bills in a list, only yesterday,
# I paid 5.90 for my Latte Macchiato. When I use your function to calculate
# the median, it simply does not work!? It returns numbers that are not even
# in the list... I don't understand what I am doing wrong.
#
# User 2: The median is defined for two cases. If "the middle" points to an
# actual index, it should be used, but when it falls "between" two values,
# the average should be used.
#
# User 3: Hahaha, you did not pay attention in your math class. Your
# calculation is plain wrong. The median of [1,2,3] is 0.3333.. fix it or I
# will stop using your function!
#
# User 4: Just because I don't have enough values in my list does not mean
# that your function can crash. It happens. Every. Time. I am furious! Wouldn't
# 'None' be a good default?

class MedianTests(TestCase):

    def test_median_works_for_single_elements(self):
        self.assertEqual(13, median([13]))

    def test_median_works_for_sorted_numbers(self):
        self.assertEqual(2, median([1, 2, 6]))

    def test_median_works_for_unsorted_numbers(self):
        self.assertEqual(2, median([6, 1, 2]))

    def test_median_works_for_odd_lists(self):
        self.assertEqual(2, median([6, 1, 2]))

    def test_median_works_for_even_lists(self):
        self.assertEqual(3, median([5, 1]))

    def test_median_works_single_even_element(self):
        self.assertEqual(None, median([]))

    def test_median_works_two_elements(self):
        self.assertEqual(1.5, median([1, 2]))

    def test_median_works_one_odd_element(self):
        self.assertEqual(5.9, median([5.9]))





