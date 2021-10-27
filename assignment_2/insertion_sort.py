class Sort(object):
    def __init__(self, array):
        self.array = array

    def insertion_sort(self):
        n = len(self.array)

        # assume array[0] is in its correct place and start the loop
        # all elements of array before jth index are sorted
        for j in range(1, n):
            # find correct position of jth element in the presorted array by comparing with the j-1th element and so on
            i = j-1
            j_elem = self.array[j]
            while i>=0 and self.array[i]>j_elem:
                # keep shifting ith element right until elem is in its correct place
                self.array[i+1] = self.array[i]
                i-=1
            # add jth element to its correct place
            self.array[i+1] = j_elem

        return self.array