import heapq

class Solution:
    def findKthLargest(self, nums, k):
        heap = []  # создаём пустую кучу
        
        for number in nums:
            heapq.heappush(heap, number)  # добавляем число
            
            # если элементов стало больше чем k
            if len(heap) > k:
                heapq.heappop(heap)  # удаляем самый маленький
        
        return heap[0]  # это k-й по величине элемент