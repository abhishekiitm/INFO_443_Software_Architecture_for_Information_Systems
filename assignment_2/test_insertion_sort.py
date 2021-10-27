import pytest

from insertion_sort import Sort

def test_insertion_sort():
    sort = Sort([0])
    result = sort.insertion_sort()

    assert result == [0]

    sort = Sort([])
    result = sort.insertion_sort()

    assert result == []

    sort = Sort([2, 4, 3, 1])
    result = sort.insertion_sort()

    assert result == [1, 2, 3, 4]

    sort = Sort([6, 10, 3, 5, 7, 2, 1, 8, 4, 9])
    result = sort.insertion_sort()

    assert result == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
