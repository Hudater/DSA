# HashMap - implementation from scratch
# Neetcode 150 - Phase 0 basics
# Concept: hash function, collision handling via chaining


class HashMap:
    def __init__(self, capacity=16):
        self.capacity = capacity
        self.size = 0
        self.buckets = [[] for _ in range(self.capacity)]  # chaining

    def _hash(self, key):
        return hash(key) % self.capacity

    def put(self, key, val):
        idx = self._hash(key)
        bucket = self.buckets[idx]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, val)  # update
                return
        bucket.append((key, val))       # insert
        self.size += 1

    def get(self, key):
        idx = self._hash(key)
        for k, v in self.buckets[idx]:
            if k == key:
                return v
        return None  # key not found

    def delete(self, key):
        idx = self._hash(key)
        bucket = self.buckets[idx]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self.size -= 1
                return

    def contains(self, key):
        return self.get(key) is not None


# --- test it ---
if __name__ == "__main__":
    hm = HashMap()
    hm.put("name", "harshit")
    hm.put("role", "sre")
    hm.put("name", "harshit mani")  # update

    print("name:", hm.get("name"))    # harshit mani
    print("role:", hm.get("role"))    # sre
    print("has 'age':", hm.contains("age"))  # False

    hm.delete("role")
    print("after delete, role:", hm.get("role"))  # None
