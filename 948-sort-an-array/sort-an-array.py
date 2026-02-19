from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # базовый случай: массив из одного элемента уже отсортирован
        if len(nums) <= 1:
            return nums
        
        # делим массив на две половины
        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        
        # сливаем отсортированные половины
        return self.merge(left, right)
    
    def merge(self, left: List[int], right: List[int]) -> List[int]:
        result = []
        i = j = 0
        
        # идём по двум массивам и добавляем меньшее число в result
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        # если что-то осталось в left
        while i < len(left):
            result.append(left[i])
            i += 1
        
        # если что-то осталось в right
        while j < len(right):
            result.append(right[j])
            j += 1
        
        return result
