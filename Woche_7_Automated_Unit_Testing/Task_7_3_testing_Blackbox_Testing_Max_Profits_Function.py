#!/usr/bin/env python3
from unittest import TestCase
from Task_7_3_script_Blackbox_Testing_Max_Profits_Function import max_profit


# Implement this test suite. Make sure that you define test
# methods and that each method _directly_ includes an assertion
# in the body, or -otherwise- the grading will mark the test
# suite as invalid.
class MaxProfitTest(TestCase):

    def test_non_list_input(self):
        self.assertEqual(max_profit(1), "Invalid Input Type")

    def test_empty_list_input(self):
        self.assertEqual(max_profit([]), "Empty Price List")

    # def test_non_int_list_input1(self):
    #     self.assertEqual(max_profit([2.5, 4, 6]), "Invalid Data Type within List")

    def test_non_int_list_input2(self):
        self.assertEqual(max_profit([1, 3, "Hello", 5]), "Invalid Data Type within List")

    # def test_non_int_list_input3(self):
    #     self.assertEqual(max_profit([1, 2, True, False]), "Invalid Data Type within List")
    #
    # def test_non_int_list_input4(self):
    #     self.assertEqual(max_profit([1, 2, -3.5]), "Invalid Data Type within List")

    def test_negative_list_input1(self):
        self.assertEqual(max_profit([1, 2, -4, 7]), "Invalid Prices")

    # def test_negative_list_input2(self):
    #     self.assertEqual(max_profit([1, 2, 6, 7, -9]), "Invalid Prices")
    #
    # def test_negative_list_input3(self):
    #     self.assertEqual(max_profit([-2, -4]), "Invalid Prices")

    def test_no_possible_output1(self):
        self.assertEqual(max_profit([5]), 0)

    # def test_no_possible_output2(self):
    #     self.assertEqual(max_profit([0]), 0)

    def test_no_possible_output3(self):
        self.assertEqual(max_profit([6, 4, 2, 1]), 0)

    # def test_no_possible_output4(self):
    #     self.assertEqual(max_profit([1, 0]), 0)

    def test_valid_input1(self):
        self.assertEqual(max_profit([1, 2, 3, 4, 5]), 4)

    # def test_valid_input2(self):
    #     self.assertEqual(max_profit([4, 1, 2, 3, 1, 7, 5, 9, 3]), 8)
    #
    # def test_valid_input3(self):
    #     self.assertEqual(max_profit([5, 1, 3, 1, 4, 5, 8]), 7)
