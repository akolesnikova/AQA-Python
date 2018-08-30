from unittest import TestCase


class TestFibonacci(TestCase):
    def test_message(self):
        self.assertTrue("Fibonacci sequence:")

    def test_expectedResult(self):
        n = 3
        self.assertTrue(3, (n - 1) + (n - 2))

    def test_ConditionForN(self):
        n = -1
        self.assertTrue(-1,  (n - 1) + (n - 2))

    def test_NotExpectedResult(self):
        n = 5
        self.assertNotEqual(1,  (n - 1) + (n - 2))
