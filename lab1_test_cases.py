import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter_ValueError(self):
        # Tests ValueError for list type None
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_max_list_iter_empty(self):
        # Tests return type of function on empty list
        tlist = []
        self.assertTrue(type(max_list_iter(tlist)), None)
    
    def test_max_list_iter_moving(self):
        # Tests correct output when largest number is in different index 
        self.assertEqual(max_list_iter([1,2,3]), 3)
        self.assertEqual(max_list_iter([1,3,2]), 3)
        self.assertEqual(max_list_iter([3,2,1]), 3)
        self.assertEqual(max_list_iter([1,1,3]), 3)
        self.assertEqual(max_list_iter([1,3,1]), 3)
       	self.assertEqual(max_list_iter([3,1,1]), 3)
        self.assertEqual(max_list_iter([3,3,3]), 3)

    def test_max_list_iter_float(self):
       	self.assertAlmostEqual(max_list_iter([1.1,2.1,3.1]), 3.1)
        self.assertAlmostEqual(max_list_iter([2.1,3.1,1.1]), 3.1)
       	self.assertAlmostEqual(max_list_iter([3.1,2.1,1.1]), 3.1)
        
    def test_reverse_rec(self):
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        self.assertEqual(reverse_rec([-1,1,0]), [0,1,-1])
        self.assertEqual(reverse_rec([1]), [1])
        
    def test_error_reverse_rec(self):
        tlist = None
        with self.assertRaises(ValueError):
             reverse_rec(tlist)
    
    def test_bin_search_empty(self):
        tlist = []        
        self.assertTrue(type(bin_search(1, 0, 10, tlist)), None)

    def test_bin_search_one(self):
        tlist = [1]
        low = 0
        high = len(tlist)-1
        self.assertEqual(bin_search(1, low, high, tlist), 0)
        
    def test_bin_search_two(self):
        tlist = [1, 2] 
        low = 0
        high = len(tlist)-1
        self.assertEqual(bin_search(2, low, high, tlist), 1) 
        self.assertEqual(bin_search(1, low, high, tlist), 0) 

    def test_bin_search_ten(self):
        tlist =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(tlist)-1
        self.assertEqual(bin_search(4, 0, len(tlist)-1, tlist), 4 )
        self.assertTrue(type(bin_search(1, 0, len(tlist)-1, tlist)), None)
        
    def test_bin_search_longer(self):
        tlist = range(100)
        low = 0
        high = len(tlist)-1
        self.assertEqual(bin_search(77, 0, len(tlist)-1, tlist), 77 )
        self.assertEqual(bin_search(0, 0, len(tlist)-1, tlist), 0 )
        self.assertEqual(bin_search(99, 0, len(tlist)-1, tlist), 99 )
        self.assertEqual(bin_search(31, 0, len(tlist)-1, tlist), 31 )

    def test_bin_search_longest(self):
        tlist = range(100000)
        low = 0
        high = len(tlist)-1
        self.assertEqual(bin_search(99501, 0, len(tlist)-1, tlist), 99501 )
        
    def test_bin_search_ValueError(self):
        tlist = None
        with self.assertRaises(ValueError):
            bin_search(2, 4, 5, tlist)
    

if __name__ == "__main__":
        unittest.main()

    
