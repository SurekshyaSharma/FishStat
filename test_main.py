from main import find_average, find_median

testArray = [1, 2, 5, 4]
testArray_1 = [1, 2, 5, 4, 7]


def test_find_average():

    assert find_average(testArray) == 3


def test_find_median():

    assert find_median(testArray_1) == 4


def test_find_median_1():
    assert find_median(testArray) == 3