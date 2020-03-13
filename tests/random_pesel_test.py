import unittest
from random_pesel.random_pesel import RandomPESEL


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.random_pesel = RandomPESEL()

    def test_random_pesel(self):
        self.assertIsInstance(self.random_pesel.generate(), str)

    def test_random_pesel_length(self):
        self.assertEqual(len(self.random_pesel.generate()), 11)

    def test_if_pesel_is_number(self):
        self.assertIsInstance(int(self.random_pesel.generate()), int)

    def test_wrong_gender(self):
        with self.assertRaises(ValueError):
            self.random_pesel.generate(gender='k')

    def test_correct_gender(self):
        self.assertIsInstance(self.random_pesel.generate(gender='m'), str)

    def test_wrong_min_age(self):
        with self.assertRaises(ValueError):
            self.random_pesel.generate(min_age=-20)

    def test_wrong_age_range(self):
        with self.assertRaises(ValueError):
            self.random_pesel.generate(min_age=20, max_age=15)


if __name__ == '__main__':
    unittest.main()
