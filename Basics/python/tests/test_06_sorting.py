import pytest
from src._06_sorting import problem_1, problem_2, problem_3, problem_4, problem_5


def test_problem_1():
    """Test Bubble Sort"""
    result = problem_1([64, 34, 25, 12, 22, 11, 90])
    if result is None:
        pytest.skip("Not implemented yet")
    assert result == [11, 12, 22, 25, 34, 64, 90]
    
    assert problem_1([1]) == [1]
    assert problem_1([]) == []
    assert problem_1([2, 1]) == [1, 2]


def test_problem_2():
    """Test Insertion Sort"""
    result = problem_2([64, 34, 25, 12, 22, 11, 90])
    if result is None:
        pytest.skip("Not implemented yet")
    assert result == [11, 12, 22, 25, 34, 64, 90]
    
    assert problem_2([1]) == [1]
    assert problem_2([]) == []
    assert problem_2([3, 3, 3]) == [3, 3, 3]


def test_problem_3():
    """Test Merge Sort"""
    result = problem_3([64, 34, 25, 12, 22, 11, 90])
    if result is None:
        pytest.skip("Not implemented yet")
    assert result == [11, 12, 22, 25, 34, 64, 90]
    
    assert problem_3([1]) == [1]
    assert problem_3([]) == []
    assert problem_3([2, 1]) == [1, 2]


def test_problem_4():
    """Test Sort Colors"""
    arr = [2, 0, 2, 1, 1, 0]
    original = arr.copy()
    problem_4(arr)
    if arr == original:
        pytest.skip("Not implemented yet")
    assert arr == [0, 0, 1, 1, 2, 2]
    
    arr = [0]
    problem_4(arr)
    assert arr == [0]


def test_problem_5():
    """Test Merge Sorted Arrays"""
    result = problem_5([1, 3, 5], [2, 4, 6])
    if result is None:
        pytest.skip("Not implemented yet")
    assert result == [1, 2, 3, 4, 5, 6]
    
    assert problem_5([], [1]) == [1]
    assert problem_5([1], []) == [1]
    assert problem_5([], []) == []