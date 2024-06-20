def parent(i):
    return i//2
def left_child(i):
    return 2*i
def right_child(i):
    return 2*i+1
class Max_Heap:
    def __init__(self): 
        self.heap = [0]
    def size(self):
        return len(self.heap)-1
    def bubble_down(self,ind):
        while left_child(ind) <= self.size():
            newInd = ind
            if self.heap[left_child(ind)] > self.heap[ind]:
                    newInd = left_child(ind)
            if right_child(ind) <= self.size() and self.heap[right_child(ind)] > self.heap[ind]:
                    newInd = right_child(ind)
            if ind == newInd:
                    break
            self.heap[ind], self.heap[newInd] = self.heap[newInd], self.heap[ind]
            ind = newInd
    def bubble_up(self,ind):
        while ind > 1 and self.heap[ind] > self.heap[parent(ind)] :
            self.heap[ind], self.heap[parent(ind)] = self.heap[parent(ind)], self.heap[ind]
            ind = parent(ind)
    def insert(self, item):
        self.heap.append(item)
        self.bubble_up(self.size())
    def get_max(self) :
        if self.size() == 0 :
            raise Exception("Heap is empty")
        return self.heap[1]
    def del_max(self) :
        if self.size() == 0 :
            raise Exception("Heap is empty")
        MAX = self.heap[1]
        self.heap[1] = self.heap[-1]
        del(self.heap[-1])
        self.bubble_down(1)
        return MAX
    def build_heap_with_bubble_up(self, L):
        self.heap = [0] + L
        for i in range(self.size()+1) :
            self.bubble_up(i)
    def build_heap_with_bubble_down(self,L):
        self.heap = [0] + L
        for i in range(self.size(),0,-1) :
            self.bubble_down(i)
    def clear(self):
        self.heap=[0]
    def heapsort(self):
        sort=[]
        while self.size() != 0 :
            MAX = self.heap[1]
            self.heap[1] = self.heap[-1]
            del(self.heap[-1])
            self.bubble_down(1)
            sort.append(MAX)
        return sort