#import numpy_financial as npf


class Quicksort:
    def __init__(self):
        pass

    def sort(self, input):
        """Sort the input list, and return the sorted list (input is unchanged)"""
        if len(input) <= 1:
            return input
        else:
            pivot = input[0]
            lt = [x for x in input if x < pivot]
            gt = [x for x in input if x > pivot]
            return self.sort(lt) + [pivot] + self.sort(gt)
    
    