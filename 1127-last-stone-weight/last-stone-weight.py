import heapq

class Solution:
    def lastStoneWeight(self, stones):
        # превращаем все веса в отрицательные, чтобы использовать min-heap как max-heap
        heap = [-stone for stone in stones]
        heapq.heapify(heap)
        
        while len(heap) > 1:
            # достаём два самых тяжёлых камня
            first = -heapq.heappop(heap)
            second = -heapq.heappop(heap)
            
            if first != second:
                # остаток возвращаем в кучу
                heapq.heappush(heap, -(first - second))
        
        # возвращаем вес последнего камня или 0, если куча пустая
        return -heap[0] if heap else 0