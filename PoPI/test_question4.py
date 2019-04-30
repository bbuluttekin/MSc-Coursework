from question4 import *

def test_1():
    assert shortest_continuous_segment([1,1,2,2,2,1,1,1]) == (1, 2)

def test_2():
    assert shortest_continuous_segment([5,5,5,2,2,2,2,3,3,3]) == (5, 3)
