from advanced_testing_techniques.quicksort import Quicksort

def test_sort_empty_array():
    qs = Quicksort()
    assert qs.sort([]) == []


def test_sort_ascending_input():
    qs = Quicksort()
    assert qs.sort([1,2,3,4]) == [1,2,3,4]


def test_sort_descending_input():
    qs = Quicksort()
    assert qs.sort([4,3,2,1]) == [1,2,3,4]


def test_arbitrary_sequence():
    qs = Quicksort()
    # bonus points if you figoure out the meaning of this input :-)
    assert qs.sort([9, 12, 19, 6]) == [6, 9, 12, 19]


def test_alternating():
    qs = Quicksort()
    assert qs.sort([1,3,2,5,4,7,6,9,8,10]) == [1,2,3,4,5,6,7,8,9,10]