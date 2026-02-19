from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # указатели на последние элементы в nums1 и nums2
        i = m - 1
        j = n - 1
        # указатель на конец nums1
        k = m + n - 1
        
        # идём с конца и ставим большее число на место
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        
        # если что-то осталось в nums2, копируем в начало nums1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
