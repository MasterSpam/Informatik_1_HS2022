
def upper_lower_capitalize(string):
    return string.upper(), string.lower(), string.capitalize()

print(upper_lower_capitalize("heLLo"))


from unittest import TestCase


class TestSuite(TestCase):

    def test_upper(self):
        self.assertEqual(upper_lower_capitalize("helLo")[0], "HELLO")

    def test_lower(self):
        self.assertEqual(upper_lower_capitalize("HElLO")[1], "hello")

    def test_capitalize(self):
        self.assertEqual(upper_lower_capitalize("hello")[2], "Hello")
