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

    def test_fibbonacci_soobin(self):
        tests = [(0, 0), (1, 1), (2, 1), (3, 2)]
        soobin = SoobinChild()

        for (n, value) in tests:
            self.assertEqual(value, soobin.fibb(n))
    
    def test_name_soobin(self):
        soobin = SoobinChild()
        suraj = SurajChild()
        self.assertNotEqual(soobin.get_name(), "Soobim")
        self.assertEqual(soobin.get_name(), "Laptop")
    
    def test_fibbonacci_suraj(self):
        tests = [(0, 0), (1, 1), (2, 1), (3, 2)]
        suraj = SurajChild()

        for (n, value) in tests:
            self.assertEqual(value, suraj.fibb(n))
    
    def test_name_suraj(self):
        suraj = SurajChild()
        self.assertNotEqual(suraj.get_name(), "Surag")
        self.assertEqual(suraj.get_name(), "Desktop")
    

class Suraj:

    def get_name(self) -> str:
        return "Suraj"

    def fibb(self, n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a+b
        return a

class SurajChild(Suraj):

    def get_name(self) -> str:
        return "Desktop"


class Primes:
    def get_name(self) -> str:
        return "Primes are unpredictable"

    def primes_below(self, n) -> int:
        length = int(n-1) // 2
        pri: list[bool] = [True] * length

        for a in range(int(n**0.5)//2):
            if pri[a]:
                pri[2*a*a+6*a+3::2*a+3] = [False] * len(range(2*a*a+6*a+3, len(pri), 2*a+3))

        return sum(pri) + 1



class PrimesTesting(unittest.TestCase):
    def test_primes(self):
        tests: list[(int, int)] = [(10, 4), (100, 25), (1000, 168)]
        
        prime = Primes()
        for (n, v) in tests:
            self.assertEqual(v, prime.primes_below(n))


if __name__ == '__main__':
    unittest.main()
