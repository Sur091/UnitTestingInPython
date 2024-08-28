# Authors:
## Soobin Yang
## Suraj Acharya

import unittest

class Soobin:

    def get_name(self) -> str:
        return "Soobim"

    # get the nth fibbonacci number
    def fibb(self, n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a+b
        return a

class SoobinChild(Soobin):

    def get_name(self) -> str:
        return "Laptop"

class FibbonacciTesting(unittest.TestCase):

    def test_fibbonacci(self):
        tests = [(0, 0), (1, 1), (2, 1), (3, 2)]
        soobin = SoobinChild()

        for (n, value) in tests:
            self.assertEqual(value, soobin.fibb(n))
    
    def test_name(self):
        soobin = SoobinChild()
        self.assertNotEqual(soobin.get_name(), "Soobim")
        self.assertEqual(soobin.get_name(), "Laptop")


if __name__ == '__main__':
    unittest.main()
