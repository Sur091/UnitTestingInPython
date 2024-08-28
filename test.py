import unittest

class Soobin(unittest.TestCase):

    def get_name(self) -> str:
        return "Soobim"
    
    # Get the number of primes below 'n'
    def number_of_primes_below(n: int):
        import numpy as np
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
    
    def test_name(self) -> None:
        self.assertEqual(self.get_name(), "Soobim")

    def test_primes(self) -> None:
        tests = [(10, 4), (100, 25), (1000, 168), (10_000, 1229), (100_000, 9592), (10**6, 78498), (10**7, 664579)]

        for (n, v) in tests:
            self.assertEqual(v, self.number_of_primes_below(n))


if __name__ == '__main__':
    unittest.main()