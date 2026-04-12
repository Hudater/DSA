"""
GRAPHS - DSA Foundations

THEORY:
Graph: Nodes (vertices) and edges, can be directed/undirected, weighted/unweighted
Representations: Adjacency list (sparse), adjacency matrix (dense)
BFS: Level-by-level, queue, shortest path unweighted, O(V+E)
DFS: Deep exploration, stack/recursion, cycle detection, O(V+E)
Patterns: Cycle detection, connected components, topological sort, shortest path
"""

from collections import deque

# ============================================================
# IMPLEMENTATION
# ============================================================

class Graph:
    """Undirected graph using adjacency list"""
    
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, u, v):
        """Add undirected edge"""
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        
        if v not in self.graph[u]:
            self.graph[u].append(v)
        if u not in self.graph[v]:
            self.graph[v].append(u)
    
    def bfs(self, start):
        """Breadth-First Search"""
        visited = set()
        queue = deque([start])
        result = []
        
        while queue:
            node = queue.popleft()
            
            if node not in visited:
                visited.add(node)
                result.append(node)
                
                if node in self.graph:
                    for neighbor in self.graph[node]:
                        if neighbor not in visited:
                            queue.append(neighbor)
        
        return result
    
    def dfs(self, start):
        """Depth-First Search"""
        visited = set()
        result = []
        
        def dfs_recursive(node):
            visited.add(node)
            result.append(node)
            
            if node in self.graph:
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        dfs_recursive(neighbor)
        
        dfs_recursive(start)
        return result


# ============================================================
# PROBLEMS
# ============================================================

def problem_1(grid):
    """Number of Islands - Count connected components"""
    pass


def problem_2(node):
    """Clone Graph - Deep copy of graph structure"""
    pass


def problem_3(num_courses, prerequisites):
    """Course Schedule - Detect cycle in directed graph"""
    pass


def problem_4(graph, start, end):
    """Shortest Path - Find minimum hops in unweighted graph"""
    pass


def problem_5(start_word, end_word, word_list):
    """Word Ladder - Shortest path between word transformations"""
    pass