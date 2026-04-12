import pytest
from src._10_graphs import problem_1, problem_2, problem_3, problem_4, problem_5


def test_problem_1():
    """Test Number of Islands"""
    grid = [['1','1','0'],
            ['1','0','0'],
            ['0','0','1']]
    result = problem_1(grid)
    if result is None:
        pytest.skip("Not implemented yet")
    assert result == 2
    
    grid = [['1','1','1'],
            ['1','1','1'],
            ['1','1','1']]
    assert problem_1(grid) == 1
    
    grid = [['0','0','0']]
    assert problem_1(grid) == 0


def test_problem_2():
    """Test Clone Graph"""
    result = problem_2(None)
    if result is None:
        pytest.skip("Not implemented yet")


def test_problem_3():
    """Test Course Schedule"""
    result = problem_3(2, [[1, 0]])
    if result is None:
        pytest.skip("Not implemented yet")
    assert result == True
    
    assert problem_3(2, [[1, 0], [0, 1]]) == False
    assert problem_3(3, [[0, 1], [0, 2], [1, 2]]) == True


def test_problem_4():
    """Test Shortest Path"""
    graph = {0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2]}
    result = problem_4(graph, 0, 2)
    if result is None:
        pytest.skip("Not implemented yet")
    assert result == 2
    
    graph = {0: [1], 1: [0, 2], 2: [1, 3], 3: [2]}
    assert problem_4(graph, 0, 3) == 3


def test_problem_5():
    """Test Word Ladder"""
    words = ["hot", "dot", "dog", "lot", "log", "cog"]
    result = problem_5("hit", "cog", words)
    if result is None:
        pytest.skip("Not implemented yet")
    assert result == 5
    
    words = ["hot", "dot", "dog", "lot", "log"]
    assert problem_5("hit", "cog", words) == 0