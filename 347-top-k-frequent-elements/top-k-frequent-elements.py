import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        
        # 1. считаем частоту каждого числа
        count = Counter(nums)
        
        heap = []
        
        # 2. добавляем элементы в кучу
        for number in count:
            frequency = count[number]
            heapq.heappush(heap, (frequency, number))
            
            # если куча больше k — удаляем самый редкий элемент
            if len(heap) > k:
                heapq.heappop(heap)
        
        # 3. собираем ответ
        result = []
        for freq, number in heap:
            result.append(number)
        
        return result