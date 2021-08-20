import unittest

from validators import validate_email


class ValidatorsTestCase(unittest.TestCase):
    def test_validate_email(self):
        self.assertTrue(validate_email('birisi@gmail.com'))


if __name__ == '__main__':
    unittest.main()
