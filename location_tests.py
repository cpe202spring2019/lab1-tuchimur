import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)         
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")

    def test_eq(self):
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("My apartment", 35.3, -120.7)
        loc3 = Location("Somehwere Elese", 31.2, -66.2)
        loc4 = 'blah'
        self.assertTrue(loc1 == loc2)
        self.assertFalse(loc1 == loc3)
        self.assertFalse(loc1 == loc4)            
    # Add more tests!

if __name__ == "__main__":
        unittest.main()
