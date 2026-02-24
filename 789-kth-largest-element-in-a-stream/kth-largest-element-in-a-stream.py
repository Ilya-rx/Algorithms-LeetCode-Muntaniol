import heapq

class KthLargest:

    def __init__(self, k, nums):
        self.k = k
        self.heap = []
        
        # добавляем начальные элементы
        for num in nums:
            heapq.heappush(self.heap, num)
            
            # если куча больше k — удаляем минимум
            if len(self.heap) > k:
                heapq.heappop(self.heap)

    def add(self, val):
        # добавляем новое число
        heapq.heappush(self.heap, val)
        
        # если элементов стало больше k
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
        # первый элемент — это k-й по величине
        return self.heap[0]