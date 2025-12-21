import unittest
from less8 import*
from main import*
class My_Test(unittest.TestCase):
    def test_args(self):
        self.assertEqual(adder(2,2),4)
    def test_kwargs(self):
        self.assertEqual(adder(a=10,b=11),21)
    def test_mixed(self):
        self.assertEqual(adder(1,a=4),3)
if __name__ == '__less8__':
    unittest.main()