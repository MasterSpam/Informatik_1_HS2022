#!/usr/bin/env python3
from unittest import TestCase
from Task_7_2_script_Roman_Number_Conversion import convert_roman_to_int


# You are supposed to develop the functionality in a test-driven way.
# Think about relevant test cases and extend the following test suite
# until all requirements of the description are covered. The test suite
# will be run against various correct and incorrect implementations, so
# make sure that you only test the `move` function and stick strictly
# to its defined signature.
#
# Make sure that you define test methods and that each method
# _directly_ includes an assertion in the body, or -otherwise- the
# grading will mark the test suite as invalid.
class ConversionTestSuite(TestCase):

    def _assert(self, roman, expected):
        actual = convert_roman_to_int(roman)
        m = f"should be {expected} but was {actual}"
        self.assertEqual(expected, actual, m)

    def test_simple_numeralI(self):
        self._assert("I", 1)

    def test_simple_numeralV(self):
        self._assert("V", 5)

    def test_simple_numeralX(self):
        self._assert("X", 10)

    def test_simple_numeralL(self):
        self._assert("L", 50)

    def test_simple_numeralC(self):
        self._assert("C", 100)

    def test_simple_numeralD(self):
        self._assert("D", 500)

    def test_simple_numeralM(self):
        self._assert("M", 1000)

    def test_simple_additive1(self):
        self._assert("XI", 11)

    def test_simple_additive2(self):
        self._assert("MD", 1500)

    def test_simple_additive3(self):
        self._assert("XIII", 13)

    def test_simple_additive4(self):
        self._assert("LXX", 70)

    def test_simple_additive5(self):
        self._assert("XXXVI", 36)

    def test_simple_additive6(self):
        self._assert("DCCLXXVII", 777)

    def test_simple_mixed1(self):
        self._assert("XIV", 14)

    def test_simple_mixed2(self):
        self._assert("XLI", 41)

    def test_simple_mixed3(self):
        self._assert("CMLIX", 959)

    def test_invalid_input1(self):          # invalid Char
        with self.assertRaises(Warning):
            convert_roman_to_int("XLS")

    def test_invalid_input2(self):          # invalid order
        with self.assertRaises(Warning):
            convert_roman_to_int("IIMX")

    def test_invalid_input3(self):          # invalid order
        with self.assertRaises(Warning):
            convert_roman_to_int("IVII")

    def test_invalid_input4(self):          # two following "special digits"
        with self.assertRaises(Warning):
            convert_roman_to_int("IXIX")

    def test_invalid_input5(self):          # four times same standard digit
        with self.assertRaises(Warning):
            convert_roman_to_int("VIIII")

    def test_invalid_input6(self):          # two times same standard digit not one
        with self.assertRaises(Warning):
            convert_roman_to_int("VV")

    def test_simple_many_m(self):           # multiple m's
        self._assert("MMMMMI", 5001)

    def test_simple_valid1(self):           # multiple m's
        self._assert("CDXC", 490)

    def test_simple_valid2(self):           # multiple m's
        self._assert("XLIX", 49)

    def test_invalid_input7(self):
        with self.assertRaises(Warning):
            convert_roman_to_int("LLX")

    def test_invalid_input8(self):
        with self.assertRaises(Warning):
            convert_roman_to_int("VIV")
