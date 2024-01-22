class MinHeap:
    def __init__(self):
        self.heap = [] #heap represented as a list

    '''
    Need to call heapify_up every time element is added
    '''
    def heapify_up(self, index):
        while index > 0: #stop once the root node is reached
            parent_index = (index - 1) // 2 #rmbr parent = (i - 1) // 2
            if self.heap[index] < self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break
    
    '''
    Need to call heapify_down every time minimum element is extracted
    '''
    def heapify_down(self, index):
        while 2*index + 1 < len(self.heap): #stop once the last element of the heap is reached
            l_idx = 2 * index
            r_idx = 2 * index + 1

            if self.heap[l_idx] <= self.heap[r_idx] and self.heap[index] > self.heap[l_idx]:
                self.heap[index], self.heap[l_idx] = self.heap[l_idx], self.heap[index]
                index = l_idx
            elif self.heap[l_idx] > self.heap[r_idx] and self.heap[index] > self.heap[r_idx]:
                self.heap[index], self.heap[r_idx] = self.heap[r_idx], self.heap[index]
                index = r_idx
            else:
                break

    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    '''
    Get minimum element and reheapify
    '''
    def get_min(self):
        if not self.heap: #don't think this ever happens but just in case
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        minn = self.heap[0] #minimum value to be returned
        self.heap[0] = self.heap.pop() #need to swap the last value in heap with root (REMEMBER?!? :D)
        self.heapify_down(0)
        return minn

    def print(self):
        print(self.heap)

heap = MinHeap()
heap.insert(4)
heap.insert(1)
heap.insert(7)
heap.insert(3)
heap.print()
