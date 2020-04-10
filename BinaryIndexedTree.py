class BinaryIndexedTree:
    def __init__(self, max_size): #n = max_size
        self.size = max_size + 1
        self.tree = [0] * self.size
    def add_to_value_at(self, index, value): #add to value at index starting from 0 O(log n)
        i = index + 1 #in tree it's from 1
        #update binary indexed tree
        while i < self.size: 
            self.tree[i] += value
            i += i & -i
    def get_sum(self, to_index, from_index = 0): # return sum of all values in the range [from_index, to_index] O(log n)
        if from_index <= 0:
            i = to_index + 1 #in tree the index runs from 1
            res = 0
            while i: # sum all tree values from 1 to i 
                res += self.tree[i]
                i -= i & - i
            return res
        else:
            return self.get_sum(to_index) - self.get_sum(from_index - 1)
    
    def get_value(self, index): #O(log n), not used in this problem, can be made O(1) using O(n) space
        return self.get_sum(to_index, to_index)
