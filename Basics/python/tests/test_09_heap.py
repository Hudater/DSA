import pytest
from src._09_heap import problem_1, problem_2, problem_3, problem_4, problem_5


def test_problem_1():
    """Test Kth Largest Element"""
    result = problem_1([3, 2, 1, 5, 6, 4], 2)
    if result is None:
        pytest.skip("Not implemented yet")
    assert result == 5
    
    assert problem_1([1], 1) == 1
    assert problem_1([1, 2, 3, 4, 5], 5) == 1
    assert problem_1([3, 1, 4, 1, 5], 3) == 3


def test_problem_2():
    """Test Top K Frequent Elements"""
    result = problem_2([1, 1, 1, 2, 2, 3], 2)
    if result is None:
        pytest.skip("Not implemented yet")
    assert sorted(result) == [1, 2]
    
    assert sorted(problem_2([1], 1)) == [1]
    assert len(problem_2([1, 1, 1, 1, 2, 2, 3], 3)) == 3


def test_problem_3():
    """Test Merge K Sorted Lists"""
    result = problem_3([[1, 4, 5], [1, 3, 4], [2, 6]])
    if result is None:
        pytest.skip("Not implemented yet")
    assert result == [1, 1, 2, 3, 4, 4, 5, 6]
    
    assert problem_3([]) == []
    assert problem_3([[1]]) == [1]


def test_problem_4():
    """Test Reorder Data in Log Files"""
    result = problem_4(["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig"])
    if result is None:
        pytest.skip("Not implemented yet")
    assert result[0].startswith("let")
    assert len(result) == 4


def test_problem_5():
    """Test Find Median from Data Stream"""
    result = problem_5()
    if result is None:
        pytest.skip("Not implemented yet")
    
    result.addNum(1)
    result.addNum(2)
    assert result.findMedian() == 1.5
    
    result.addNum(3)
    assert result.findMedian() == 2