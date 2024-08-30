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

class SoobinPrime(Soobin):

    def get_name(self) -> str:
        return "Primes are the best."

    # Get the number of primes less that n
    def primes_less_than(self, n: int) -> int:
        import numpy as np
        # Get the number of primes below 'n'
        length_of_sieve = int(n - 1) // 2

        # A boolean list for odd numbers
        primes_list = np.full(length_of_sieve, True)

        index_of_square_root_of_n: int = int(n ** 0.5) // 2

        # Sieve
        for a in range(index_of_square_root_of_n):
            if primes_list[a]:
                index_of_a_squared: int = 2*a*a + 6*a + 3
                step: int = 2*a + 3
                primes_list[index_of_a_squared::step] = False

        # The odd number is prime if at the corresponding index we have the value True
        return np.sum(primes_list) + 1

class PrimeTesting(unittest.TestCase):

    def test_name(self):
        soobin_prime = SoobinPrime()
        self.assertEqual(soobin_prime.get_name(), "Primes are the best.")

    def test_primes(self):
        soobin_prime = SoobinPrime()
        self.assertEqual(soobin_prime.primes_less_than(10), 4)

if __name__ == '__main__':
    unittest.main()
