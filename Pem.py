import unittest
from Addition import addition

class UnitTest(unittest.TestCase):
    def test_addition(self):
        addition_instance = addition()
        self.assertEqual(10, addition_instance.addition(8, 2))
if __name__=="__main__":
    unittest.main()

        
