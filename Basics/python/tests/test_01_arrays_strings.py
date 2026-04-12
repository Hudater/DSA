import pytest
from src._01_arrays_strings import problem_1, problem_2, problem_3, problem_4, problem_5


def test_problem_1():
    """Test Two Sum"""
    result = problem_1([2, 7, 11, 15], 9)
    if result is None:
        pytest.skip("Not implemented yet")
    assert sorted(result) == [0, 1]
    
    result = problem_1([3, 2, 4], 6)
    assert sorted(result) == [1, 2]
    
    result = problem_1([0, 0], 0)
    assert sorted(result) == [0, 1]


def test_problem_2():
    """Test Valid Palindrome"""
    result = problem_2("A man, a plan, a canal: Panama")
    if result is None:
        pytest.skip("Not implemented yet")
    assert result == True
    
    assert problem_2("race a car") == False
    assert problem_2(" ") == True
    assert problem_2("a") == True


def test_problem_3():
    """Test Reverse String"""
    s = ['h', 'e', 'l', 'l', 'o']
    original = s.copy()
    problem_3(s)
    if s == original:
        pytest.skip("Not implemented yet")
    assert s == ['o', 'l', 'l', 'e', 'h']
    
    s = ['a']
    problem_3(s)
    assert s == ['a']
    
    s = []
    problem_3(s)
    assert s == []


def test_problem_4():
    """Test Remove Duplicates"""
    arr = [1, 1, 2, 2, 3]
    result = problem_4(arr)
    if result is None:
        pytest.skip("Not implemented yet")
    assert result == 3
    assert arr[:result] == [1, 2, 3]
    
    arr = [1]
    assert problem_4(arr) == 1
    
    arr = []
    assert problem_4(arr) == 0


def test_problem_5():
    """Test Rotate Array"""
    arr = [1, 2, 3, 4, 5]
    original = arr.copy()
    problem_5(arr, 2)
    if arr == original:
        pytest.skip("Not implemented yet")
    assert arr == [4, 5, 1, 2, 3]
    
    arr = [1]
    problem_5(arr, 1)
    assert arr == [1]
    
    arr = [1, 2, 3]
    problem_5(arr, 0)
    assert arr == [1, 2, 3]