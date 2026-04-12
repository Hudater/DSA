# DSA Foundations - Complete Package

A comprehensive Python package for mastering **62 core DSA concepts** across 10 fundamental topics.

## 📁 Folder Structure

```txt
python/
├── src/
│   ├── __init__.py
│   ├── _01_arrays_strings.py
│   ├── _02_hashmap.py
│   ├── _03_stack_queue.py
│   ├── _04_linked_list.py
│   ├── _05_recursion.py
│   ├── _06_sorting.py
│   ├── _07_binary_search.py
│   ├── _08_binary_tree.py
│   ├── _09_heap.py
│   └── _10_graphs.py
├── tests/
│   ├── test_01_arrays_strings.py
│   ├── test_02_hashmap.py
│   ├── test_03_stack_queue.py
│   ├── test_04_linked_list.py
│   ├── test_05_recursion.py
│   ├── test_06_sorting.py
│   ├── test_07_binary_search.py
│   ├── test_08_binary_tree.py
│   ├── test_09_heap.py
│   └── test_10_graphs.py
├── pyproject.toml
└── README.md
```

## 🚀 Setup

### Using `uv` (Recommended)

```bash
# Install uv if not already installed
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create virtual environment and install dependencies
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dev dependencies (includes pytest)
uv pip install -e ".[dev]"
```

## ✅ Running Tests

### Run All Tests

```bash
pytest tests/ -v
```

### Run Tests for Specific Topic

```bash
pytest tests/test_01_arrays_strings.py -v
pytest tests/test_02_hashmap.py -v
pytest tests/test_03_stack_queue.py -v
pytest tests/test_04_linked_list.py -v
pytest tests/test_05_recursion.py -v
pytest tests/test_06_sorting.py -v
pytest tests/test_07_binary_search.py -v
pytest tests/test_08_binary_tree.py -v
pytest tests/test_09_heap.py -v
pytest tests/test_10_graphs.py -v
```

### Run Tests for Specific Problem

```bash
pytest tests/test_01_arrays_strings.py::test_problem_1 -v
```

### Show Skipped Tests (Not Implemented Yet)

```bash
pytest tests/ -v -rs
```

## 📚 Study Order

Complete topics in this **recommended sequence**:

### Phase 1: Fundamentals (Weeks 1-3)

1. **Arrays & Strings** (`src/_01_arrays_strings.py`) - 5 problems
    - Two Sum, Valid Palindrome, Reverse String, Remove Duplicates, Rotate Array

2. **Hashmap** (`src/_02_hashmap.py`) - 8 problems
    - Two Sum, Valid Anagram, Group Anagrams, Contains Duplicate, Majority Element, Ransom Note, Isomorphic Strings, First Unique Character

3. **Stack & Queue** (`src/_03_stack_queue.py`) - 8 problems
    - Valid Parentheses, Min Stack, Decode String, Largest Rectangle, Queue from Stacks, Daily Temperatures, Recent Calls, Trapping Rain Water

### Phase 2: Linked Structures (Weeks 4-5)

4. **Linked List** (`src/_04_linked_list.py`) - 8 problems
    - Reverse, Detect Cycle, Find Middle, Merge Sorted, Remove Nth, Partition, Palindrome, Swap Pairs

5. **Recursion** (`src/_05_recursion.py`) - 5 problems
    - Power, Sum of Array, Find Maximum, Count Occurrences, Generate Permutations

### Phase 3: Advanced Algorithms (Weeks 6-8)

6. **Sorting** (`src/_06_sorting.py`) - 5 problems
    - Bubble Sort, Insertion Sort, Merge Sort, Sort Colors, Merge Arrays

7. **Binary Search** (`src/_07_binary_search.py`) - 5 problems
    - Search in Sorted Array, First/Last Position, Insert Position, Peak Element, Count Occurrences

8. **Binary Tree** (`src/_08_binary_tree.py`) - 8 problems
    - Max Depth, Invert Tree, Same Tree, Symmetric Tree, Level Order, Path Sum, LCA in BST, Validate BST

9. **Heap** (`src/_09_heap.py`) - 5 problems
    - Kth Largest, Top K Frequent, Merge K Lists, Reorder Log Files, Median Stream

10. **Graphs** (`src/_10_graphs.py`) - 5 problems
    - Number of Islands, Clone Graph, Course Schedule, Shortest Path, Word Ladder

**Total: 62 Problems to Master**

## 📖 How to Use

### For Each Topic:

1. **Read Theory** (in docstring)
    - Core concepts
    - Time/Space complexity
    - When to use
    - Common patterns

2. **Study Implementation**
    - Reference implementations in each file
    - Understand the patterns
    - Don't memorize, understand "why"

3. **Implement Problems**
    - Replace `pass` with your solution
    - Don't look at implementation first
    - Try multiple approaches
    - Test locally with pytest

4. **Run Tests**

    ```bash
    pytest tests/test_0X_[topic].py -v
    ```

    - See which test cases fail
    - Learn from failures
    - Tests show SKIPPED until you implement (that's normal!)

5. **Optimize & Refactor**
    - Can you improve time complexity?
    - Reduce space complexity?
    - Code readability?
    - Try alternative approaches?

## 🎯 What Each Test Shows

Tests use **pytest** framework with these conventions:

```python
def test_problem_1():
    result = problem_1([2, 7, 11, 15], 9)
    if result is None:
        pytest.skip("Not implemented yet")  # ⏭️ SKIPPED
    assert sorted(result) == [0, 1]         # ✅ PASSED or ❌ FAILED
```

### Test Status Meanings:

- **SKIPPED** ⏭️ - Function returns None (you haven't implemented yet) - **This is expected!**
- **PASSED** ✅ - Your implementation passed this test case
- **FAILED** ❌ - Your implementation didn't pass, debug needed

## 📊 Problem Breakdown

| Topic   | File                    | Problems        | Topics                                                         |
| ------- | ----------------------- | --------------- | -------------------------------------------------------------- |
| Phase 1 | `_01_arrays_strings.py` | 5               | Two Sum, Palindrome, Reverse, Remove Duplicates, Rotate        |
|         | `_02_hashmap.py`        | 8               | Two Sum, Anagrams, Duplicates, Majority Element, etc           |
|         | `_03_stack_queue.py`    | 8               | Brackets, Min Stack, Decode String, Histogram, etc             |
| Phase 2 | `_04_linked_list.py`    | 8               | Reverse, Cycle, Middle, Merge, Partition, Palindrome           |
|         | `_05_recursion.py`      | 5               | Power, Sum, Max, Count, Permutations                           |
| Phase 3 | `_06_sorting.py`        | 5               | Bubble, Insertion, Merge, Colors, Merge Arrays                 |
|         | `_07_binary_search.py`  | 5               | Search, First/Last, Insert Pos, Peak, Count                    |
|         | `_08_binary_tree.py`    | 8               | Depth, Invert, Symmetric, Level Order, Path Sum, LCA, Validate |
|         | `_09_heap.py`           | 5               | Kth Largest, Top K Frequent, Merge K Lists, Reorder, Median    |
|         | `_10_graphs.py`         | 5               | Islands, Clone, Course Schedule, Shortest Path, Word Ladder    |
|         |                         | **62 Problems** | **10 Core Patterns**                                           |

## 💡 Key Patterns by Topic

### Arrays & Strings

- Two pointers
- Sliding window
- In-place modifications

### Hashmap

- Frequency counting
- Complement checking
- Grouping

### Stack & Queue

- Monotonic stacks
- Bracket matching
- BFS vs DFS

### Linked List

- Dummy node trick
- Two pointers (slow/fast)
- Reversal

### Recursion

- Base cases (critical!)
- Memoization
- Backtracking

### Sorting

- Bubble, insertion, merge
- Partition
- Merge sorted arrays

### Binary Search

- Off-by-one errors
- Finding first/last
- Insertion point

### Binary Tree

- Tree traversals (DFS, BFS)
- BST properties
- Path problems

### Heap

- Heap operations
- K-th element
- Merging

### Graphs

- BFS vs DFS
- Cycle detection
- Shortest path

## ⚡ Quick Start Example

```bash
# 1. Setup
uv venv
source .venv/bin/activate
uv pip install -e ".[dev]"

# 2. Study a topic
# Read src/_01_arrays_strings.py theory and implementation

# 3. Implement a problem
# Edit src/_01_arrays_strings.py, replace problem_1(pass) with your code

# 4. Run tests
pytest tests/test_01_arrays_strings.py::test_problem_1 -v

# 5. Debug if needed, optimize, move to next problem
```

## ✨ Expected Test Output

Before implementing (all skipped):

```txt
test_01_arrays_strings.py::test_problem_1 SKIPPED
test_01_arrays_strings.py::test_problem_2 SKIPPED
...
```

After implementing problem_1:

```txt
test_01_arrays_strings.py::test_problem_1 PASSED
test_01_arrays_strings.py::test_problem_2 SKIPPED
...
```

After implementing all problems:

```txt
test_01_arrays_strings.py::test_problem_1 PASSED
test_01_arrays_strings.py::test_problem_2 PASSED
test_01_arrays_strings.py::test_problem_3 PASSED
test_01_arrays_strings.py::test_problem_4 PASSED
test_01_arrays_strings.py::test_problem_5 PASSED
...
========================= 5 passed in 0.05s ==========================
```

## 📁 File Naming Convention

- **Source files**: `src/_0X_topic_name.py` (underscore prefix for valid Python module naming)
- **Test files**: `tests/test_0X_topic_name.py`
- **Package**: `src/__init__.py` marks src as a Python package

This naming convention:
✅ Keeps numbered ordering (09, 10, etc. work as expected)  
✅ Valid Python identifiers (no leading numbers in module names)  
✅ Easy to sort and navigate

## 🎓 After Completing This Package

1. **Review** (Week 9)
    - Go back to hard problems
    - Try different approaches
    - Optimize for time/space

2. **Combination** (Week 10)
    - Mix problems from multiple topics
    - Real-world scenarios
    - Interview-style problems

3. **NeetCode 150** (Week 11+)
    - Move to advanced practice
    - Recognize patterns instantly
    - Time pressure practice

4. **Real Interviews**
    - Explain while coding
    - Ask clarifying questions
    - Discuss trade-offs

## 🚨 Common Mistakes to Avoid

- ❌ Memorizing solutions (understand instead)
- ❌ Copy-pasting code (type it out manually)
- ❌ Skipping edge cases (empty, single element, negatives)
- ❌ Ignoring time/space complexity
- ❌ Not understanding the theory first
- ❌ Rushing through just to finish

## ✅ Best Practices

- ✅ **Type manually** - Forces understanding
- ✅ **Explain out loud** - Cement the concepts
- ✅ **Test edge cases** - Day 1, not last day
- ✅ **Draw diagrams** - Especially for trees/graphs
- ✅ **Try multiple approaches** - Learn different ways
- ✅ **Refactor after passing** - Make code cleaner
- ✅ **Review difficult problems** - Revisit weekly

## 🤔 FAQ

**Q: Tests show SKIPPED status, is that bad?**  
A: No! SKIPPED means your function returned None (still `pass`). That's expected. Implement the function and the test will run.

**Q: How long does this take?**  
A: 4-6 weeks serious study (~2-3 hours daily). Adjust based on your pace.

**Q: Should I do all 62 problems?**  
A: Yes, but don't rush. Quality > Speed. Deep understanding matters more than quantity.

**Q: Can I skip a topic?**  
A: Not recommended. Each topic builds on previous concepts. Follow the study order.

**Q: What if I get stuck?**  
A: 1) Re-read theory, 2) Study implementation, 3) Walk through example manually, 4) Try different approach, 5) Revisit later.

**Q: Why the underscore prefix in file names?**  
A: Python doesn't allow module names starting with numbers. Underscore prefix (`_01_`) keeps ordering while being valid identifiers. The `src/__init__.py` makes it a proper package.

## 📝 Checklist

- [ ] Phase 1 Complete (5 + 8 + 8 = 21 problems)
- [ ] Phase 2 Complete (8 + 5 = 13 problems)
- [ ] Phase 3 Complete (5 + 5 + 8 + 5 + 5 = 28 problems)
- [ ] All 62 Tests Passing ✅
- [ ] Able to Explain Each Pattern
- [ ] Ready for NeetCode 150

## 💬 Remember

> "The goal is not to memorize solutions, but to understand the problem-solving approach and apply these techniques to new problems."
