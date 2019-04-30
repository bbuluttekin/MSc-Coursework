from question3 import *


def test_1():
    t789 = ManhattanTaxi(5, 5, 1, 30)
    assert t789.moveto(3, 9) == True
    assert t789.pos[0] == 3 and t789.pos[1] == 9
    assert abs(t789.fuel - 24) < 0.01
