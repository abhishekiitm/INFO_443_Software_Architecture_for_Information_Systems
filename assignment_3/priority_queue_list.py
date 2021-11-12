import math

class MinPriorityQueue(object):
    """
    This class implementats the abstract data type - priority queue
    Underlying data structure used is a list based heap implementation

    Attributes:
      queue list
    
    Methods:
      is_empty()
      find_min()
      delete_min()
      insert(num)
      make_empty()
    """
    def __init__(self, array):
        """
        initializes a min priority queue from any unordered list 

        Parameters:
          array list
        """
        self.queue = array
        # start from the middle as the leaves already satisfy the heap property
        n_start = math.floor(len(self.queue)/2)-1
        
        # heapify the non leaf elements starting from the second lowest level to the root level
        for idx in range(n_start, -1, -1):
            self._min_heapify(idx)

    def _min_heapify(self, idx):
        left_idx = 2*(idx+1)-1
        right_idx = left_idx + 1
        if left_idx < len(self.queue) and right_idx < len(self.queue):
            swap_idx = left_idx if self.queue[left_idx] < self.queue[right_idx] else right_idx
        elif left_idx < len(self.queue):
            swap_idx = left_idx
        else:
            return
        if self.queue[swap_idx] < self.queue[idx]:
            temp = self.queue[idx]
            self.queue[idx] = self.queue[swap_idx]
            self.queue[swap_idx] = temp
            self._min_heapify(swap_idx)

    def is_empty(self):
        return (True if len(self.queue) == 0  else False)

    def find_min(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return "Priority Queue is empty"

    def delete_min(self):
        if self.is_empty():
            print ("The list is empty and there is no element to delete.")
            return
        self.queue[0] = self.queue[-1]
        del self.queue[-1]
        self._min_heapify(0)

    def insert(self, num):
        self.queue.append(num)
        parent_idx = math.floor(len(self.queue)/2)-1
        idx = len(self.queue) - 1
        condition = True if ((parent_idx >= 0) and self.queue[parent_idx] > num) else False
        while condition:
            self.queue[idx] = self.queue[parent_idx]
            idx = parent_idx
            parent_idx = math.floor((parent_idx-1)/2)
            condition = True if ((parent_idx >= 0) and self.queue[parent_idx] > num) else False
        self.queue[idx] = num

    def make_empty(self):
        self.queue = []
