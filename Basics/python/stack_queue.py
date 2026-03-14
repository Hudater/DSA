# Stack + Queue - implementation from scratch
# Neetcode 150 - Phase 0 basics


# --- Stack (LIFO) ---
class Stack:
    def __init__(self):
        self._data = []

    def push(self, val):
        self._data.append(val)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._data.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)


# --- Queue (FIFO) using two stacks ---
class Queue:
    def __init__(self):
        self._inbox = []   # push here
        self._outbox = []  # pop from here

    def enqueue(self, val):
        self._inbox.append(val)

    def dequeue(self):
        if not self._outbox:
            while self._inbox:
                self._outbox.append(self._inbox.pop())
        if not self._outbox:
            raise IndexError("Queue is empty")
        return self._outbox.pop()

    def peek(self):
        if not self._outbox:
            while self._inbox:
                self._outbox.append(self._inbox.pop())
        if not self._outbox:
            raise IndexError("Queue is empty")
        return self._outbox[-1]

    def is_empty(self):
        return not self._inbox and not self._outbox


# --- test it ---
if __name__ == "__main__":
    s = Stack()
    s.push(1); s.push(2); s.push(3)
    print("Stack peek:", s.peek())   # 3
    print("Stack pop:", s.pop())     # 3
    print("Stack pop:", s.pop())     # 2

    q = Queue()
    q.enqueue(1); q.enqueue(2); q.enqueue(3)
    print("Queue dequeue:", q.dequeue())  # 1
    print("Queue dequeue:", q.dequeue())  # 2
    q.enqueue(4)
    print("Queue dequeue:", q.dequeue())  # 3
