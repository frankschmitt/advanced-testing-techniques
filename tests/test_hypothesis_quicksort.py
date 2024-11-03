from hypothesis import given, strategies as st  
from hypothesis import assume as hypothesis_assume  
  
from advanced_testing_techniques.quicksort import quicksort

# Property Based Unit Testing  
@given(st.lists(st.integers(), min_size=0, max_size=25))  
def test_quicksort_same_result_as_library_sort(input_list):
    assert quicksort(input_list) == sorted(input_list)