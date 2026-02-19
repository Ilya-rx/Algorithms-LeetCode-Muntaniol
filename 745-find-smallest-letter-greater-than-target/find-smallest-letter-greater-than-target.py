from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left = 0
        right = len(letters) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if letters[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        # если вышли за границу массива,
        # значит подходящей буквы нет
        if left < len(letters):
            return letters[left]
        else:
            return letters[0]
   