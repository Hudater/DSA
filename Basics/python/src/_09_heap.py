"""
HEAP / PRIORITY QUEUE - DSA Foundations

THEORY:
Heap: Complete binary tree satisfying heap property
Min Heap: Parent ≤ children, root is minimum
Max Heap: Parent ≥ children, root is maximum
Operations: Push/Pop/Peek O(log n), Heapify O(n)
Python's heapq: MIN heap only, use negation for max heap
Use: Priority queues, k-th element, Dijkstra, Huffman coding
vs Sorted list: O(log n) insert vs O(n)
"""

import heapq

# ============================================================
# IMPLEMENTATION
# ============================================================

class MinHeap:
    """Min heap using list"""
    
    def __init__(self):
        self.heap = []
    
    def push(self, val):
        """Add and maintain heap property"""
        heapq.heappush(self.heap, val)
    
    def pop(self):
        """Remove and return minimum"""
        return heapq.heappop(self.heap) if self.heap else None
    
    def peek(self):
        """View minimum"""
        return self.heap[0] if self.heap else None
    
    def size(self):
        """Return element count"""
        return len(self.heap)


class MaxHeap:
    """Max heap using negation with min heap"""
    
    def __init__(self):
        self.heap = []
    
    def push(self, val):
        """Add element (negate for max)"""
        heapq.heappush(self.heap, -val)
    
    def pop(self):
        """Remove and return maximum"""
        return -heapq.heappop(self.heap) if self.heap else None
    
    def peek(self):
        """View maximum"""
        return -self.heap[0] if self.heap else None


# ============================================================
# PROBLEMS
# ============================================================

def problem_1(arr, k):
    """Kth Largest Element - Find kth largest value"""
    pass


def problem_2(arr, k):
    """Top K Frequent Elements - Find k most common elements"""
    pass


def problem_3(lists):
    """Merge K Sorted Lists - Combine multiple sorted sequences"""
    pass


def problem_4(logs):
    """Reorder Data in Log Files - Custom sorting with stable sort"""
    pass


def problem_5():
    """Find Median from Data Stream - Efficient median calculation"""
    pass