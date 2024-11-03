from advanced_testing_techniques.quicksort import quicksort

import unittest

class QuicksortTestCase(unittest.TestCase):
    def test_sort_empty_array(self):
        assert quicksort([]) == []

    def test_sort_ascending_input(self):
        assert quicksort([1,2,3,4]) == [1,2,3,4]

    def test_sort_descending_input(self):
        assert quicksort([4,3,2,1]) == [1,2,3,4]

    def test_arbitrary_sequence(self):
        # bonus points if you figoure out the meaning of this input :-)
        assert quicksort([9, 12, 19, 6]) == [6, 9, 12, 19]

    def test_alternating(self):
        assert quicksort([1,3,2,5,4,7,6,9,8,10]) == [1,2,3,4,5,6,7,8,9,10]
