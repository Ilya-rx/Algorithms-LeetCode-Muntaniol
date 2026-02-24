import heapq

class Solution:
    def kClosest(self, points, k):
        
        heap = []
        
        # добавляем все точки в кучу
        for x, y in points:
            distance = x*x + y*y
            heapq.heappush(heap, (distance, [x, y]))
        
        result = []
        
        # берём k ближайших точек
        for _ in range(k):
            distance, point = heapq.heappop(heap)
            result.append(point)
        
        return result