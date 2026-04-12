import pytest
from src._02_hashmap import problem_1, problem_2, problem_3, problem_4, problem_5, problem_6, problem_7, problem_8


def test_problem_1():
    """Test Two Sum"""
    result = problem_1([2, 7, 11, 15], 9)
    if result is None:
        pytest.skip("Not implemented yet")
    assert sorted(result) == [0, 1]
    
    assert sorted(problem_1([3, 2, 4], 6)) == [1, 2]
    assert sorted(problem_1([3, 3], 6)) == [0, 1]
    assert sorted(problem_1([-1, -2, -3, 5, 10], 7)) == [3, 4]


def test_problem_2():
    """Test Valid Anagram"""
    result = problem_2("anagram", "nagaram")
    if result is None:
        pytest.skip("Not implemented yet")
    assert result == True
    
    assert problem_2("abc", "bca") == True
    assert problem_2("abc", "abd") == False
    assert problem_2("", "") == True


def test_problem_3():
    """Test Group Anagrams"""
    result = problem_3(["eat", "tea", "tan", "ate", "nat", "bat"])
    if result is None:
        pytest.skip("Not implemented yet")
    assert len(result) == 3
    
    assert problem_3(["a"]) == [["a"]]
    assert len(problem_3(["abc", "def", "ghi"])) == 3
    assert len(problem_3(["ab", "ba", "aa"])) == 2


def test_problem_4():
    """Test Contains Duplicate"""
    result = problem_4([1, 2, 3, 1])
    if result is None:
        pytest.skip("Not implemented yet")
    assert result == True
    
    assert problem_4([1, 1]) == True
    assert problem_4([1, 2, 3, 4]) == False
    assert problem_4([]) == False


def test_problem_5():
    """Test Majority Element"""
    result = problem_5([3, 2, 3])
    if result is None:
        pytest.skip("Not implemented yet")
    assert result == 3
    
    assert problem_5([2, 2, 1, 1, 1, 2, 2]) == 2
    assert problem_5([1]) == 1
    assert problem_5([-1, -1, -1, 2]) == -1


def test_problem_6():
    """Test Ransom Note"""
    result = problem_6("a", "a")
    if result is None:
        pytest.skip("Not implemented yet")
    assert result == True
    
    assert problem_6("a", "b") == False
    assert problem_6("aa", "aab") == True
    assert problem_6("", "abc") == True


def test_problem_7():
    """Test Isomorphic Strings"""
    result = problem_7("egg", "add")
    if result is None:
        pytest.skip("Not implemented yet")
    assert result == True
    
    assert problem_7("badc", "baba") == False
    assert problem_7("a", "b") == True
    assert problem_7("abc", "abc") == True


def test_problem_8():
    """Test First Unique Character"""
    result = problem_8("leetcode")
    if result is None:
        pytest.skip("Not implemented yet")
    assert result == 0
    
    assert problem_8("loveleetcode") == 2
    assert problem_8("aabb") == -1
    assert problem_8("a") == 0