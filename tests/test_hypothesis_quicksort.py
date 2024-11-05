from hypothesis import given, strategies as st  
from hypothesis import assume as hypothesis_assume  
  
from advanced_testing_techniques.quicksort import quicksort

# Property Based Unit Testing  
@given(st.lists(st.integers(), min_size=0, max_size=25))  
def test_quicksort_is_idempotent(input_list):
    assert quicksort(quicksort(input_list)) == quicksort(input_list)

@given(st.lists(st.integers(), min_size=0, max_size=25))  
def test_quicksort_keeps_length_of_input_list(input_list):
    assert len(quicksort(input_list)) == len(input_list)
