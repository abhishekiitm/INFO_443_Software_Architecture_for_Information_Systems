import math

class TreeNode(object):
    """
    Implements a single node of a tree
    """
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self, level=0):
        ret = "\t"*level+repr(self.value)+"\n"
        for child in (self.left, self.right):
            if child is not None:
                ret += child.__repr__(level+1)
        return ret


class MinPriorityQueue(object):
    """
    This class implementats the abstract data type - priority queue
    Underlying data structure used is a tree based heap implementation

    Attributes:
      root TreeNode
      heap_size int

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
        self.heap_size = 0
        for elem in array:
            self.insert(elem, heapify=False)

        n_start = math.floor(self.heap_size/2)
        for idx in range(n_start, 0, -1):
            node = self._get_node(n_start)
            self._min_heapify(node)

    def _min_heapify(self, node):
        left_node = node.left
        right_node = node.right
        if left_node is not None and right_node is not None:
            swap_node = left_node if left_node.value < right_node.value else right_node
        elif left_node is not None:
            swap_node = left_node
        else:
            return
        if swap_node.value < node.value:
            temp = node.value
            node.value = swap_node.value
            swap_node.value = temp
            self._min_heapify(swap_node)

    def _get_path_to_node(self, node_number):
        path_to_node = []
        while node_number != 1:
            path_to_node.append(node_number)
            node_number = math.floor(node_number/2)
        path_to_node.reverse()
        return path_to_node
    
    def _get_node(self, destination_node_number):
        """
        returns the node of the heap tree that corresponds the the destination_node_number
        """
        if destination_node_number < 1:
            return None
        path_to_node = self._get_path_to_node(destination_node_number)
        node = self.root
        for node_number in path_to_node:
            # left node is always even numbered whereas right node is odd 
            node = node.left if node_number%2 == 0 else node.right
        return node

    def is_empty(self):
        return (True if self.heap_size == 0  else False)

    def find_min(self):
        if not self.is_empty():
            return self.root.value
        else:
            return "Priority Queue is empty"

    def delete_min(self):
        if self.heap_size <= 1:
            self.root = None
            self.heap_size = 0
            return
        last_node = self._get_node(self.heap_size)
        last_node_parent = self._get_node(math.floor(self.heap_size/2))
        self.root.value = last_node.value
        if self.heap_size % 2 == 0:
            last_node_parent.left = None
        else:
            last_node_parent.right = None
        self.heap_size -= 1
        self._min_heapify(self.root)
    
    def insert(self, num, heapify=True):
        if self.heap_size == 0:
            self.root = TreeNode(num)
            self.heap_size += 1
            return
        
        parent_node_number = math.floor((self.heap_size+1)/2)
        parent_node = self._get_node(parent_node_number)
        child_node = TreeNode(num)
        
        if (self.heap_size+1) % 2 == 0:
            parent_node.left = child_node
        else:
            parent_node.right = child_node
        self.heap_size += 1

        if heapify:
            condition = True if ((parent_node is not None) and parent_node.value > num) else False
            while condition:
                child_node.value = parent_node.value
                child_node = parent_node
                parent_node_number = math.floor(parent_node_number/2)
                parent_node = self._get_node(parent_node_number)
                condition = True if ((parent_node is not None) and parent_node.value > num) else False
            child_node.value = num

    def make_empty(self):
        self.root = None
        self.heap_size = 0
