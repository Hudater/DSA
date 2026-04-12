import pytest
from collections import deque
from src._08_binary_tree import TreeNode, problem_1, problem_2, problem_3, problem_4, problem_5, problem_6, problem_7, problem_8


def create_binary_tree(values):
    """Helper to create tree from level order list"""
    if not values or values[0] is None:
        return None
    
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(values):
        node = queue.popleft()
        
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    
    return root


def test_problem_1():
    """Test Maximum Depth"""
    root = create_binary_tree([3, 9, 20, None, None, 15, 7])
    result = problem_1(root)
    if result is None:
        pytest.skip("Not implemented yet")
    assert result == 3
    
    assert problem_1(None) == 0
    assert problem_1(create_binary_tree([1])) == 1
    assert problem_1(create_binary_tree([1, 2, None, 3])) == 3


def test_problem_2():
    """Test Invert Binary Tree"""
    root = create_binary_tree([4, 2, 7, 1, 3, 6, 9])
    result = problem_2(root)
    if result is None:
        pytest.skip("Not implemented yet")
    assert result.val == 4
    
    assert problem_2(None) is None
    assert problem_2(create_binary_tree([1])).val == 1


def test_problem_3():
    """Test Same Tree"""
    p = create_binary_tree([1, 2, 3])
    q = create_binary_tree([1, 2, 3])
    result = problem_3(p, q)
    if result is None:
        pytest.skip("Not implemented yet")
    assert result == True
    
    p = create_binary_tree([1, 2])
    q = create_binary_tree([1, None, 2])
    assert problem_3(p, q) == False
    
    assert problem_3(None, None) == True


def test_problem_4():
    """Test Symmetric Tree"""
    root = create_binary_tree([1, 2, 2, 3, 4, 4, 3])
    result = problem_4(root)
    if result is None:
        pytest.skip("Not implemented yet")
    assert result == True
    
    root = create_binary_tree([1, 2, 2, None, 3, None, 3])
    assert problem_4(root) == False
    
    assert problem_4(None) == True


def test_problem_5():
    """Test Level Order Traversal"""
    root = create_binary_tree([3, 9, 20, None, None, 15, 7])
    result = problem_5(root)
    if result is None:
        pytest.skip("Not implemented yet")
    assert result == [[3], [9, 20], [15, 7]]
    
    assert problem_5(None) == []
    assert problem_5(create_binary_tree([1])) == [[1]]


def test_problem_6():
    """Test Path Sum"""
    root = create_binary_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, 1])
    result = problem_6(root, 22)
    if result is None:
        pytest.skip("Not implemented yet")
    assert result == True
    
    root = create_binary_tree([1, 2, 3])
    assert problem_6(root, 5) == False
    
    assert problem_6(None, 0) == False


def test_problem_7():
    """Test Lowest Common Ancestor in BST"""
    root = create_binary_tree([6, 2, 8, 0, 4, 7, 9])
    result = problem_7(root, 2, 8)
    if result is None:
        pytest.skip("Not implemented yet")
    assert result.val == 6
    
    assert problem_7(root, 2, 4).val == 2
    assert problem_7(root, 0, 9).val == 6


def test_problem_8():
    """Test Validate BST"""
    root = create_binary_tree([2, 1, 3])
    result = problem_8(root)
    if result is None:
        pytest.skip("Not implemented yet")
    assert result == True
    
    root = create_binary_tree([5, 1, 4, None, None, 3, 6])
    assert problem_8(root) == False
    
    assert problem_8(create_binary_tree([1])) == True