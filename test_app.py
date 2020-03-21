import unittest

import app


# App Logic Unit Tests
class TestAppLogic(unittest.TestCase):

    # Test Client List Generator Function Output Sum
    def test_numberGeneratorSum(self):
        self.assertEqual(sum(app.generateNumberList()), 50000005000000)


if __name__ == '__main__':
    unittest.main()
