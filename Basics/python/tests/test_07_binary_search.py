import pytest
from src._07_binary_search import problem_1, problem_2, problem_3, problem_4, problem_5


def test_problem_1():
    """Test Search in Sorted Array"""
    result = problem_1([1, 3, 5, 7, 9], 5)
    if result is None:
        pytest.skip("Not implemented yet")
    assert result == 2
    
    assert problem_1([1, 3, 5, 7, 9], 1) == 0
    assert problem_1([1, 3, 5, 7, 9], 9) == 4
    assert problem_1([1, 3, 5, 7, 9], 4) == -1


def test_problem_2():
    """Test Find First and Last Position"""
    result = problem_2([5, 7, 7, 8, 8, 10], 8)
    if result is None:
        pytest.skip("Not implemented yet")
    assert result == [3, 4]
    
    assert problem_2([5, 7, 7, 8, 8, 10], 5) == [0, 0]
    assert problem_2([5, 7, 7, 8, 8, 10], 7) == [1, 2]
    assert problem_2([5, 7, 7, 8, 8, 10], 6) == [-1, -1]


def test_problem_3():
    """Test Search Insert Position"""
    result = problem_3([1, 3, 5, 6], 5)
    if result is None:
        pytest.skip("Not implemented yet")
    assert result == 2
    
    assert problem_3([1, 3, 5, 6], 4) == 2
    assert problem_3([1, 3, 5, 6], 0) == 0
    assert problem_3([1, 3, 5, 6], 7) == 4


def test_problem_4():
    """Test Peak Element"""
    result = problem_4([1, 3, 4, 5, 4, 2, 1])
    if result is None:
        pytest.skip("Not implemented yet")
    assert result == 3
    
    assert problem_4([1, 2, 1]) == 1
    assert problem_4([3, 2, 1]) == 0
    assert problem_4([1, 2, 3]) == 2


def test_problem_5():
    """Test Count Occurrences"""
    result = problem_5([5, 7, 7, 8, 8, 8, 10], 8)
    if result is None:
        pytest.skip("Not implemented yet")
    assert result == 3
    
    assert problem_5([5, 7, 7, 8, 8, 8, 10], 7) == 2
    assert problem_5([5, 7, 7, 8, 8, 8, 10], 5) == 1
    assert problem_5([5, 7, 7, 8, 8, 8, 10], 6) == 0