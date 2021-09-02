import pytest
from code.Reverse_Number import reverse


def test_reverse_num_positive():
    val = reverse(3456)
    assert val == 6543

def test_reverse_num_negative():
    val = reverse(-4539)
    assert val == -9354




