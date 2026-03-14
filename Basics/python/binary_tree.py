# Binary Tree - implementation from scratch
# Neetcode 150 - Phase 0 basics
# Topics: insert (BST), BFS (level order), DFS (inorder/preorder/postorder)

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
            return
        curr = self.root
        while True:
            if val < curr.val:
                if not curr.left:
                    curr.left = TreeNode(val)
                    return
                curr = curr.left
            else:
                if not curr.right:
                    curr.right = TreeNode(val)
                    return
                curr = curr.right

    # BFS - level order traversal
    def bfs(self):
        if not self.root:
            return []
        result = []
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

    # DFS - inorder (left → root → right) → sorted for BST
    def inorder(self, node=None, first=True):
        if first:
            node = self.root
        if not node:
            return []
        return self.inorder(node.left, False) + [node.val] + self.inorder(node.right, False)

    # DFS - preorder (root → left → right)
    def preorder(self, node=None, first=True):
        if first:
            node = self.root
        if not node:
            return []
        return [node.val] + self.preorder(node.left, False) + self.preorder(node.right, False)

    # DFS - postorder (left → right → root)
    def postorder(self, node=None, first=True):
        if first:
            node = self.root
        if not node:
            return []
        return self.postorder(node.left, False) + self.postorder(node.right, False) + [node.val]


# --- test it ---
if __name__ == "__main__":
    bst = BinarySearchTree()
    for v in [5, 3, 7, 1, 4, 6, 8]:
        bst.insert(v)

    print("BFS:", bst.bfs())          # [5, 3, 7, 1, 4, 6, 8]
    print("Inorder:", bst.inorder())  # [1, 3, 4, 5, 6, 7, 8] - sorted!
    print("Preorder:", bst.preorder()) # [5, 3, 1, 4, 7, 6, 8]
    print("Postorder:", bst.postorder()) # [1, 4, 3, 6, 8, 7, 5]
