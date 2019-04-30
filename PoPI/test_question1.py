from question1 import *

def test_1():
    assert number_of_above_averages(2,2, [[1,1], [2,4]])== 1

def test_2():
    assert number_of_above_averages(2,3, [[1,2,3], [4,5,6]]) == 3
