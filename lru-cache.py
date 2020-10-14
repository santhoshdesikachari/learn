"""
Implement LRU cache using Doubly linked list backed by Dict.
"""

# Node
class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    def __str__(self):
        return str(self.key) + ' ~> ' + str(self.value)


#LRU Cache
class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {} # value is a node in the linked list

        self.head = Node(0, 0)
        self.tail = Node(1, 1)

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        v = -1
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            node = self._add(node.key, node.value)
            v = node.value
        return v

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            v = node.value
            self._remove(node)
            node = self._add(key, v)
            self.cache[key] = node
        else:
            node = self._add(key, value)
            self.cache[key] = node

    def _add(self, key, value):
        if len(self.cache) >= self.capacity and self.tail.prev != self.head:
                self._remove(self.tail.prev)

        node = Node(key, value)
        first = self.head.next
        node.prev = self.head
        node.next = first
        first.prev = node
        self.head.next = node
        return node

    def _remove(self, node):
        if node == self.head or node == self.tail:
            return

        left = node.prev
        right = node.next

        left.next = right
        right.prev = left

        del self.cache[node.key]

    def __str__(self):
        node = self.head
        output = ''
        while node is not None:
            output = output + '(' + str(node) + ')'
            node = node.next
        return output

#Driver
cache = LRUCache(3)

print('adding items to cache')
cache.put(100, 100)
cache.put(200, 200)
cache.put(300, 300)
cache.put(400, 400)
cache.put(500, 500)

print(cache.get(100))

print('what is in cache?')
print(cache)
