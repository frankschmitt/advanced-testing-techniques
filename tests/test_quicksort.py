from advanced_testing_techniques.quicksort import Quicksort

def test_sort_empty_array():
    qs = Quicksort()
    assert qs.sort([]) == []


def test_sort_ascending_input():
    qs = Quicksort()
    assert qs.sort([1,2,3,4]) == [1,2,3,4]
