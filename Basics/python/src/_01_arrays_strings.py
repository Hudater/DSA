"""
ARRAYS & STRINGS - DSA Foundations

THEORY:
Arrays: Contiguous memory, O(1) access, O(n) insertion/deletion
Strings: Immutable sequences, similar to arrays
Key Patterns: Two-pointer, sliding window, in-place modifications
Time: Access O(1), Search O(n), Insert/Delete O(n), Append O(1) amortized
When to use: Ordered collections, fast random access, as foundation for other DS
"""

# ============================================================
# IMPLEMENTATION
# ============================================================

class DynamicArray:
    """Simple dynamic array implementation"""
    def __init__(self):
        self.size = 0
        self.capacity = 1
        self.array = [None] * self.capacity
    
    def append(self, value):
        """Add element, resize if needed"""
        if self.size == self.capacity:
            self.capacity *= 2
            new_array = [None] * self.capacity
            for i in range(self.size):
                new_array[i] = self.array[i]
            self.array = new_array
        
        self.array[self.size] = value
        self.size += 1
    
    def get(self, index):
        """Get element at index"""
        if 0 <= index < self.size:
            return self.array[index]
        return None
    
    def to_list(self):
        """Convert to Python list"""
        return self.array[:self.size]


# ============================================================
# PROBLEMS
# ============================================================

def problem_1(nums, target):
    """Two Sum - Find two indices that sum to target"""
    pass


def problem_2(s):
    """Valid Palindrome - Check if string is palindrome (ignore spaces/case)"""
    pass


def problem_3(s):
    """Reverse String - Reverse array in-place"""
    pass


def problem_4(nums):
    """Remove Duplicates - Remove duplicates from sorted array in-place"""
    pass


def problem_5(nums, k):
    """Rotate Array - Rotate array right by k positions"""
    pass