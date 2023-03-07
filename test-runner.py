import unittest
import importlib

class TestAssignmentOne(unittest.TestCase):
    def test_01_calculate_movie_minutes(self):
        self.assertEqual(asgmt.calculate_movie_minutes(2, 22), 142)
        self.assertEqual(asgmt.calculate_movie_minutes(2, 55), 175)
        self.assertEqual(asgmt.calculate_movie_minutes(2, 32), 152)
        self.assertEqual(asgmt.calculate_movie_minutes(2, 1), 121)
        self.assertEqual(asgmt.calculate_movie_minutes(1, 2), 62)
    def test_02_convert_kilometers_to_miles(self):
        self.assertTrue(asgmt.convert_kilometers_to_miles(42.195) >= 26)
        self.assertTrue(asgmt.convert_kilometers_to_miles(21.095) >= 13)
        self.assertTrue(asgmt.convert_kilometers_to_miles(10) >= 6)
        self.assertTrue(asgmt.convert_kilometers_to_miles(5) >= 3)
        self.assertTrue(asgmt.convert_kilometers_to_miles(1) >= 0.6)
    def test_03_calculate_bmi(self):
        self.assertTrue(asgmt.calculate_bmi(216, 147) >= 31)
        self.assertTrue(asgmt.calculate_bmi(206, 113) >= 26)
        self.assertTrue(asgmt.calculate_bmi(211, 110) >= 24)
        self.assertTrue(asgmt.calculate_bmi(180, 65) >= 20)
        self.assertTrue(asgmt.calculate_bmi(170, 65) >= 22)
    def test_04_format_movie_time(self):
        self.assertEqual(asgmt.format_movie_time(2, 22), "2 hours 22 minutes")
        self.assertEqual(asgmt.format_movie_time(2, 55), "2 hours 55 minutes")
        self.assertEqual(asgmt.format_movie_time(2, 32), "2 hours 32 minutes")
        self.assertEqual(asgmt.format_movie_time(2, 10), "2 hours 10 minutes")
        self.assertEqual(asgmt.format_movie_time(2, 20), "2 hours 20 minutes")
    def test_05_format_temperature_degrees(self):
        self.assertEqual(asgmt.format_temperature_degrees(0), "0 Degrees Celsius = 32.0 Degrees Fahrenheit")
        self.assertEqual(asgmt.format_temperature_degrees(100), "100 Degrees Celsius = 212.0 Degrees Fahrenheit")
    def test_06_format_integer_with_dollar_sign_and_commas(self):
        self.assertEqual(asgmt.format_integer_with_dollar_sign_and_commas(1000), "$1,000")
        self.assertEqual(asgmt.format_integer_with_dollar_sign_and_commas(1000000), "$1,000,000")
        self.assertEqual(asgmt.format_integer_with_dollar_sign_and_commas(1000000000), "$1,000,000,000")
        self.assertEqual(asgmt.format_integer_with_dollar_sign_and_commas(10000), "$10,000")
        self.assertEqual(asgmt.format_integer_with_dollar_sign_and_commas(100000), "$100,000")
    def test_07_is_positive(self):
        self.assertFalse(asgmt.is_positive(-2))
        self.assertFalse(asgmt.is_positive(-1))
        self.assertFalse(asgmt.is_positive(0))
        self.assertTrue(asgmt.is_positive(1))
        self.assertTrue(asgmt.is_positive(2))
    def test_08_is_even(self):
        self.assertFalse(asgmt.is_even(1))
        self.assertFalse(asgmt.is_even(3))
        self.assertFalse(asgmt.is_even(5))
        self.assertTrue(asgmt.is_even(0))
        self.assertTrue(asgmt.is_even(2))
    def test_09_are_vowels_contained(self):
        self.assertFalse(asgmt.are_vowels_contained('pythn'))
        self.assertFalse(asgmt.are_vowels_contained('ncnd'))
        self.assertFalse(asgmt.are_vowels_contained('rtclt'))
        self.assertTrue(asgmt.are_vowels_contained('anaconda'))
        self.assertTrue(asgmt.are_vowels_contained('reticulate'))
    def test_10_are_all_vowels_contained(self):
        self.assertFalse(asgmt.are_all_vowels_contained('python'))
        self.assertFalse(asgmt.are_all_vowels_contained('anaconda'))
        self.assertFalse(asgmt.are_all_vowels_contained('reticulate'))
        self.assertTrue(asgmt.are_all_vowels_contained('anaconda and reticulate'))
        self.assertTrue(asgmt.are_all_vowels_contained('aeiou'))

asgmt = importlib.import_module("asgmt-one")
suite = unittest.TestLoader().loadTestsFromTestCase(TestAssignmentOne)
runner = unittest.TextTestRunner(verbosity=2)
test_results = runner.run(suite)
number_of_failures = len(test_results.failures)
number_of_errors = len(test_results.errors)
number_of_test_runs = test_results.testsRun
number_of_successes = number_of_test_runs - (number_of_failures + number_of_errors)
print("You've got {} successes among {} questions.".format(number_of_successes, number_of_test_runs))