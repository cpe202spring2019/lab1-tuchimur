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
        # Tests correct output with floating point list items 
       	self.assertAlmostEqual(max_list_iter([1.1,2.1,3.1]), 3.1)
        self.assertAlmostEqual(max_list_iter([2.1,3.1,1.1]), 3.1)
       	self.assertAlmostEqual(max_list_iter([3.1,2.1,1.1]), 3.1)
        
    def test_reverse_rec(self):
        # Tests good working order with three-item list
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        self.assertEqual(reverse_rec([-1,1,0]), [0,1,-1])
    def test_reverse_rec_one(self):
        # Tests good working order with one-item list
        self.assertEqual(reverse_rec([1]), [1])
        
    def test_reverse_rec_two(self):
        # Tests good working order with two-item list
        self.assertEqual(reverse_rec([1,2]), [2,1])
      
    def test_error_reverse_rec(self):
        # Tests value error on none-type list
        tlist = None
        with self.assertRaises(ValueError):
             reverse_rec(tlist)
    
    def test_bin_search_empty(self):
        # Tests return type none on empty list
        tlist = []        
        self.assertTrue(type(bin_search(1, 0, 10, tlist)), None)

    def test_bin_search_one(self):
        # tests good working order of one-item list
        tlist = [1]
        low = 0
        high = len(tlist)-1
        self.assertEqual(bin_search(1, low, high, tlist), 0)
        
    def test_bin_search_two(self):
        # two-item list
        tlist = [1, 2] 
        low = 0
        high = len(tlist)-1
        self.assertEqual(bin_search(2, low, high, tlist), 1) 
        self.assertEqual(bin_search(1, low, high, tlist), 0) 

    def test_bin_search_ten(self):
        # ten-item list
        tlist =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(tlist)-1
        self.assertEqual(bin_search(4, 0, len(tlist)-1, tlist), 4 )
        
    def test_bin_search_longer(self):
        # tests 100 item list with various targets
        tlist = range(100)
        low = 0
        high = len(tlist)-1
        self.assertEqual(bin_search(77, 0, len(tlist)-1, tlist), 77 )
        self.assertEqual(bin_search(0, 0, len(tlist)-1, tlist), 0 )
        self.assertEqual(bin_search(99, 0, len(tlist)-1, tlist), 99 )
        self.assertEqual(bin_search(31, 0, len(tlist)-1, tlist), 31 )

    def test_bin_search_missing(self):
        # tests for failure on target not in list
        tlist = range(10)
        self.assertTrue(type(bin_search(50, 0, 9, tlist)), None)
    
    def test_bin_search_longest(self):
        # tests 100,000 item list for target
        tlist = range(100000)
        low = 0
        high = len(tlist)-1
        self.assertEqual(bin_search(99501, 0, len(tlist)-1, tlist), 99501 )
        
    def test_bin_search_ValueError(self):
        # tests for value error on none-type input
        tlist = None
        with self.assertRaises(ValueError):
            bin_search(2, 4, 5, tlist)
    

if __name__ == "__main__":
        unittest.main()

    
