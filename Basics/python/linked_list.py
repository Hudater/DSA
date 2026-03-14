# Linked List - implementation from scratch
# Neetcode 150 - Phase 0 basics
# Topics: Node, insert (head/tail), delete, traversal, reverse


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node

    def insert_at_tail(self, val):
        node = Node(val)
        if not self.head:
            self.head = node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node

    def delete(self, val):
        if not self.head:
            return
        if self.head.val == val:
            self.head = self.head.next
            return
        curr = self.head
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
                return
            curr = curr.next

    def traverse(self):
        curr = self.head
        result = []
        while curr:
            result.append(curr.val)
            curr = curr.next
        return result

    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev


# --- test it ---
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_tail(1)
    ll.insert_at_tail(2)
    ll.insert_at_tail(3)
    ll.insert_at_head(0)
    print("After inserts:", ll.traverse())   # [0, 1, 2, 3]

    ll.delete(2)
    print("After delete 2:", ll.traverse())  # [0, 1, 3]

    ll.reverse()
    print("After reverse:", ll.traverse())   # [3, 1, 0]
