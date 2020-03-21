import unittest

import app


# App Logic Unit Tests
class TestAppLogic(unittest.TestCase):

    # Test Client List Generator Function Output Sum
    def test_numberGeneratorSum(self):
        self.assertEqual(sum(app.generateNumberList()), 50000005000000, "List Number Function Produced Invalid Sum")

    # Test List Item Int checker is functional
    def test_checkListItemsAreInt(self):
        self.assertEqual(app.checkListItemsAreInt([1, 2, 3]), True, "List Item Check Failed on [1, 2, 3]")
        self.assertEqual(app.checkListItemsAreInt(["A", "B", "C"]), False, "List Item Check Failed on [A, B, C]")
        self.assertEqual(app.checkListItemsAreInt([]), True, "List Item Check Failed on []")  # Allowed as sum is 0
        self.assertEqual(app.checkListItemsAreInt([9132.12, 123.1, 0.00005]), False, "List Item Check Failed on"
                                                                                     "[9132.12, 123.1, 0.00005]")


if __name__ == '__main__':
    unittest.main()
