
# implement minHeap
class PriorityQueue(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.heap = [0] * (self.capacity + 1)
        self.heap[0] = -9223372036854775807
        self.FIRST = 1
        self.size = 0

    def __str__(self):
        return str(self.heap[1:])

    def put(self, value):
        if self.size > self.capacity:
            return
        else:
            self.size += 1
            self.heap[self.size] = value

            current = self.size
            while self.heap[current] < self.heap[self._parent_pos(current)]:
                self._swap(current, self._parent_pos(current))
        self._heapify()

    def min(self):
        return self.heap[self.FIRST]

    def pop_min(self):
        v = self.heap[self.FIRST]
        self.heap[self.FIRST] = self.heap[self.size]
        self.size -= 1
        self._min_heapify(self.FIRST)
        self.heap = self.heap[:-1]
        return v

    def _left_child_pos(self, i):
        return 2 * i

    def _right_child_pos(self, i):
        return 2 * i + 1

    def _parent_pos(self, i):
        return i//2

    def _swap(self, l_pos, r_pos):
        self.heap[l_pos], self.heap[r_pos] = self.heap[r_pos], self.heap[l_pos]

    def _is_leaf(self, i):
        if i >= self.size//2 and i <= self.size:
            return True
        else:
            return False

    def _min_heapify(self, i):
        if not self._is_leaf(i):
            left_child_pos = self._left_child_pos(i)
            right_child_pos = self._right_child_pos(i)
            if (self.heap[i] > self.heap[left_child_pos] or
                self.heap[i] > self.heap[right_child_pos]):

                if self.heap[left_child_pos] < self.heap[right_child_pos]:
                    self._swap(i, left_child_pos)
                    self._min_heapify(left_child_pos)
                else:
                    self._swap(i, right_child_pos)
                    self._min_heapify(right_child_pos)

    def _heapify(self):
        for i in range(self.size//2, 0, -1):
            self._min_heapify(i)

# Driver code
q = PriorityQueue(7)

q.put(100)
q.put(41)
q.put(31)
q.put(13)
q.put(16)
q.put(41)
q.put(51)

print('original heap: ' + str(q))
print('minimum value: ' + str(q.min()))
print('remove min: ' + str(q.pop_min()))
print('heap: ' + str(q))
print('remove min: ' + str(q.pop_min()))
print('heap: ' + str(q))
