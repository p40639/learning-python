import unittest
import trytry

class Testtrytry(unittest.TestCase):

    def test_add(self):
        self.assertEqual(trytry.add(3,4), 7)
    
    def test_factorial(self):
        self.assertEqual(trytry.factorial(3), 6)


if __name__ == '__main__':
    unittest.main()