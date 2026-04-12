"""
BINARY SEARCH - DSA Foundations

THEORY:
Binary Search: Efficient search for sorted arrays, O(log n)
Eliminates half per iteration using divide & conquer
Variants: Exact value, first/last occurrence, closest value, insertion point
Key: Must have sorted data, careful with boundaries, mid = left + (right-left)//2
Mistakes: Off-by-one errors, integer overflow, not handling edge cases
When: Fast lookup needed, monotonic property exists
"""

# ============================================================
# IMPLEMENTATION
# ============================================================

def binary_search_iterative(arr, target):
    """Standard binary search (iterative)"""
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


def find_first_occurrence(arr, target):
    """Find leftmost occurrence (handles duplicates)"""
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            result = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result


# ============================================================
# PROBLEMS
# ============================================================

def problem_1(arr, target):
    """Search in Sorted Array - Standard binary search"""
    pass


def problem_2(arr, target):
    """Find First and Last Position - Find range of target occurrence"""
    pass


def problem_3(arr, target):
    """Search Insert Position - Find target or insertion point"""
    pass


def problem_4(arr):
    """Peak Element - Find mountain peak efficiently"""
    pass


def problem_5(arr, target):
    """Count Occurrences - Count frequency using binary search"""
    pass