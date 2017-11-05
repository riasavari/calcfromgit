import unittest
import calc


class Testcalc(unittest.TestCase):

    def test_add(self):
        result=calc.add(10,5)
        self.assertEqual(result, 15)
        # alt use the following:
        self.assertEqual(calc.add(10, 5), 15)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)

        self.assertRaises(ValueError, calc.divide, 10, 0)
        # alt use the following with context manager:
        with self.assertRaises(ValueError):
            calc.divide(10, 0)

if __name__ == '__main__':
    unittest.main()
