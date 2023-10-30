import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [11, 12, 22, 25, 34, 64, 90]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)

def test_bubble_sort_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [90, 64, 34, 25, 22, 12, 11]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)

def test_bubble_sort_is_zero():
    result = []
    input_arr = []

    result = Lab3.bubble_sort(input_arr, 3)

    assert (result == 0)

def test_bubble_sort_check_integer():
    result = []
    input_arr = [50, 20, 50.23, 60, 80.2]

    result = Lab3.bubble_sort(input_arr, 3)

    assert (result == 2)

def test_bubble_sort_more_than_ten():
    result = []
    input_arr = [50, 20, 50, 60, 80, 30, 21, 58, 83, 49, 57, 20]

    result = Lab3.bubble_sort(input_arr, 3)

    assert (result == 1)