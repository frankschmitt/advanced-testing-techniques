from advanced_testing_techniques.quicksort import quicksort

import unittest

class QuicksortBadTestCase(unittest.TestCase):

    def test_quicksort_bad(self):
        quicksort([1,2,3,4])
        assert(1 == 1)