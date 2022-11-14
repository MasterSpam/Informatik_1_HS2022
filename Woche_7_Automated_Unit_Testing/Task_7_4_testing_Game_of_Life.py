#!/usr/bin/env python3
from unittest import TestCase
from Task_7_4_script_Game_of_Life import evolve


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
class EvolveTestSuite(TestCase):

    def test_glider(self):
        field = (
            "--------------",
            "|            |",
            "|  ###       |",
            "|  #         |",
            "|   #        |",
            "|            |",
            "--------------"
        )
        expected = ((
                        "--------------",
                        "| ###        |",
                        "| #          |",
                        "|  #         |",
                        "|            |",
                        "|            |",
                        "--------------"
                    ), 5)
        actual = evolve(field, 4)
        self.assertEqual(actual, expected)

    def test_no_string_as_line1(self):
        field = (
            ["--------------"],
            "|            |",
            "|  ###       |",
            "|  #         |",
            "|   #        _",
            "|            |",
            "--------------"
        )
        with self.assertRaises(Warning):
            evolve(field, 4)

    def test_invalid_char1(self):
        field = (
            "--------------",
            "|            |",
            "|  ###       |",
            "|  #         |",
            "|   #        _",
            "|            |",
            "--------------"
        )
        with self.assertRaises(Warning):
            evolve(field, 4)

    def test_different_line_length(self):
        field = (
            "-------------",
            "|            |",
            "|  ###       |",
            "|  #         |",
            "|   #        |",
            "|            |",
            "--------------"
        )
        with self.assertRaises(Warning):
            evolve(field, 4)

    def test_too_small_world1(self):
        field = (
            "--",
            "||",
            "||",
            "||",
            "||",
            "||",
            "--"
        )
        with self.assertRaises(Warning):
            evolve(field, 4)

    def test_too_small_world2(self):
        field = (
            "-------",
            "-------"
        )
        with self.assertRaises(Warning):
            evolve(field, 4)

    def test_not_int_as_step1(self):
        field = (
            "--------------",
            "|            |",
            "|  ###       |",
            "|  #         |",
            "|   #        _",
            "|            |",
            "--------------"
        )
        with self.assertRaises(Warning):
            evolve(field, 4.5)

    def test_negative_int_as_step1(self):
        field = (
            "--------------",
            "|            |",
            "|  ###       |",
            "|  #         |",
            "|   #        _",
            "|            |",
            "--------------"
        )
        with self.assertRaises(Warning):
            evolve(field, -3)

    def test_empty_world1(self):
        field = ()
        with self.assertRaises(Warning):
            evolve(field, -3)

    def test_char_at_wrong_position1(self):
        field = (
            "--------------",
            "|            |",
            "|  ###       |",
            "|  #         |",
            "|   #        |",
            "|       |    |",
            "--------------"
        )
        with self.assertRaises(Warning):
            evolve(field, 4)

    def test_char_at_wrong_position2(self):
        field = (
            "--------------",
            "|            |",
            "|  ###       |",
            "|  #         |",
            "|   #        |",
            "|            -",
            "--------------"
        )
        with self.assertRaises(Warning):
            evolve(field, 4)





