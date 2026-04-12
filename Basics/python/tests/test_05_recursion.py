import pytest
from src._05_recursion import problem_1, problem_2, problem_3, problem_4, problem_5


def test_problem_1():
    """Test Power"""
    result = problem_1(2, 10)
    if result is None:
        pytest.skip("Not implemented yet")
    assert result == 1024
    
    assert problem_1(2.0, -2) == 0.25
    assert problem_1(1, 1000) == 1
    assert problem_1(-1, 3) == -1


def test_problem_2():
    """Test Sum of Array"""
    result = problem_2([1, 2, 3, 4, 5])
    if result is None:
        pytest.skip("Not implemented yet")
    assert result == 15
    
    assert problem_2([]) == 0
    assert problem_2([5]) == 5
    assert problem_2([-1, -2, -3]) == -6


def test_problem_3():
    """Test Find Maximum"""
    result = problem_3([3, 7, 2, 9, 1])
    if result is None:
        pytest.skip("Not implemented yet")
    assert result == 9
    
    assert problem_3([1]) == 1
    assert problem_3([-5, -2, -10]) == -2
    assert problem_3([0, 0, 0]) == 0


def test_problem_4():
    """Test Count Occurrences"""
    result = problem_4([1, 2, 2, 3, 2], 2)
    if result is None:
        pytest.skip("Not implemented yet")
    assert result == 3
    
    assert problem_4([1, 1, 1], 1) == 3
    assert problem_4([1, 2, 3], 4) == 0
    assert problem_4([], 1) == 0


def test_problem_5():
    """Test Generate Permutations"""
    result = problem_5([1, 2, 3])
    if result is None:
        pytest.skip("Not implemented yet")
    assert len(result) == 6
    assert [1, 2, 3] in result
    assert [3, 2, 1] in result
    
    assert problem_5([1]) == [[1]]