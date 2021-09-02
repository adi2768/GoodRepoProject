import pytest

def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    sum1 = 0

    if x > 0:
        n = len(str(x))
        for i in range(n):
            rem = x % 10
            x = x // 10
            sum1 = (sum1 * 10) + rem
        return sum1

    elif x < 0:
        x = x * -1
        n = len(str(x))
        for i in range(0, n):
            rem = x % 10
            x = x // 10
            sum1 = (sum1 * 10) + rem
        return sum1 * -1

    else:
        return x

def test_reverse_num_case1():
    val = reverse(123)
    assert val == 321

def test_reverse_num_case2():
    val = reverse(3)
    assert val == 3

def test_reverse_num_case3():
    val = reverse(-4539)
    assert val == -9354

def test_reverse_num_case4():
    val = reverse(67)
    assert val == 76

def test_reverse_num_case5():
    val = reverse(-456)
    assert val == -654

def test_reverse_num_case6():
    val = reverse(-111)
    assert val == -111




