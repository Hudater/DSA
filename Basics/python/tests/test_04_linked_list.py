import pytest
from src._04_linked_list import Node, problem_1, problem_2, problem_3, problem_4, problem_5, problem_6, problem_7, problem_8


def create_linked_list(arr):
    """Helper to create linked list from array"""
    if not arr:
        return None
    head = Node(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = Node(val)
        curr = curr.next
    return head


def linked_list_to_array(head):
    """Helper to convert linked list to array"""
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result


def test_problem_1():
    """Test Reverse Linked List"""
    head = create_linked_list([1, 2, 3])
    result = problem_1(head)
    if result is None:
        pytest.skip("Not implemented yet")
    assert linked_list_to_array(result) == [3, 2, 1]
    
    assert problem_1(None) is None
    assert linked_list_to_array(problem_1(create_linked_list([1]))) == [1]
    assert linked_list_to_array(problem_1(create_linked_list([1, 2]))) == [2, 1]


def test_problem_2():
    """Test Detect Cycle"""
    head = create_linked_list([1, 2, 3])
    result = problem_2(head)
    if result is None:
        pytest.skip("Not implemented yet")
    assert result == False
    
    assert problem_2(None) == False
    
    head = create_linked_list([1])
    assert problem_2(head) == False
    
    head = Node(1)
    head.next = Node(2)
    head.next.next = head
    assert problem_2(head) == True


def test_problem_3():
    """Test Find Middle"""
    head = create_linked_list([1, 2, 3, 4, 5])
    result = problem_3(head)
    if result is None:
        pytest.skip("Not implemented yet")
    assert result.val == 3
    
    head = create_linked_list([1, 2, 3, 4])
    assert problem_3(head).val in [2, 3]
    
    head = create_linked_list([1])
    assert problem_3(head).val == 1


def test_problem_4():
    """Test Merge Two Sorted Lists"""
    head1 = create_linked_list([1, 3, 5])
    head2 = create_linked_list([2, 4, 6])
    result = problem_4(head1, head2)
    if result is None:
        pytest.skip("Not implemented yet")
    assert linked_list_to_array(result) == [1, 2, 3, 4, 5, 6]
    
    head1 = create_linked_list([1, 2, 3])
    assert linked_list_to_array(problem_4(head1, None)) == [1, 2, 3]
    
    assert problem_4(None, None) is None


def test_problem_5():
    """Test Remove Nth Node From End"""
    head = create_linked_list([1, 2, 3, 4, 5])
    result = problem_5(head, 2)
    if result is None:
        pytest.skip("Not implemented yet")
    assert linked_list_to_array(result) == [1, 2, 3, 5]
    
    head = create_linked_list([1, 2])
    assert linked_list_to_array(problem_5(head, 2)) == [2]
    
    head = create_linked_list([1])
    assert problem_5(head, 1) is None


def test_problem_6():
    """Test Partition List"""
    head = create_linked_list([1, 4, 3, 2, 5, 2])
    result = problem_6(head, 3)
    if result is None:
        pytest.skip("Not implemented yet")
    arr = linked_list_to_array(result)
    assert len(arr) == 6
    
    head = create_linked_list([1, 2, 2])
    assert linked_list_to_array(problem_6(head, 5)) == [1, 2, 2]


def test_problem_7():
    """Test Palindrome Linked List"""
    head = create_linked_list([1, 2, 3, 2, 1])
    result = problem_7(head)
    if result is None:
        pytest.skip("Not implemented yet")
    assert result == True
    
    assert problem_7(create_linked_list([1, 2, 2, 1])) == True
    assert problem_7(create_linked_list([1])) == True
    assert problem_7(create_linked_list([1, 2, 3])) == False


def test_problem_8():
    """Test Swap Nodes in Pairs"""
    head = create_linked_list([1, 2, 3, 4])
    result = problem_8(head)
    if result is None:
        pytest.skip("Not implemented yet")
    assert linked_list_to_array(result) == [2, 1, 4, 3]
    
    assert linked_list_to_array(problem_8(create_linked_list([1, 2, 3]))) == [2, 1, 3]
    assert linked_list_to_array(problem_8(create_linked_list([1]))) == [1]